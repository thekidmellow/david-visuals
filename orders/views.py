from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.conf import settings
from django.urls import reverse
from packages.models import Package
import stripe

stripe.api_key = settings.STRIPE_SECRET_KEY


@login_required
def checkout(request, package_id):
    package = get_object_or_404(Package, pk=package_id, is_active=True)

    context = {
        'package': package,
        'stripe_public_key': settings.STRIPE_PUBLIC_KEY,
    }
    return render(request, 'orders/checkout.html', context)


@login_required
def create_checkout_session(request, package_id):
    package = get_object_or_404(Package, pk=package_id, is_active=True)

    try:
        checkout_session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[{
                'price_data': {
                    'currency': 'eur',
                    'unit_amount': int(package.price * 100),
                    'product_data': {
                        'name': package.name,
                        'description': package.description[:100],
                    },
                },
                'quantity': 1,
            }],
            mode='payment',
            success_url=request.build_absolute_uri(
                reverse('orders:success')
            ) + '?session_id={CHECKOUT_SESSION_ID}',
            cancel_url=request.build_absolute_uri(reverse('orders:cancel')),
            client_reference_id=package_id,
            metadata={
                'package_id': package_id,
                'user_id': request.user.id,
            }
        )
        return redirect(checkout_session.url, code=303)
    except Exception as e:
        print(f"Stripe Error: {str(e)}")
        messages.error(request, f'Payment setup failed. Please try again.')
        return redirect('orders:checkout', package_id=package_id)


@login_required
def success(request):
    session_id = request.GET.get('session_id')

    if session_id:
        try:
            session = stripe.checkout.Session.retrieve(session_id)
            package_id = session.client_reference_id
            package = Package.objects.get(pk=package_id)

            from .models import Order
            order = Order.objects.create(
                user=request.user,
                package=package,
                total=package.price,
                stripe_pid=session.payment_intent,
                status='completed'
            )

            messages.success(
                request,
                f'Payment successful! '
                f'Your order number is {order.order_number}'
            )
            context = {
                'order': order,
                'package': package,
            }
            return render(request, 'orders/success.html', context)
        except Exception as e:
            print(f"Success page error: {str(e)}")
            messages.error(
                request, 'There was an error processing your order.'
            )
            return redirect('packages:package_list')

    return redirect('packages:package_list')


@login_required
def cancel(request):
    messages.warning(request, 'Payment was cancelled.')
    return render(request, 'orders/cancel.html')
