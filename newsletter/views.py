from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Subscriber
from .forms import SubscriberForm


def subscribe(request):
    if request.method == 'POST':
        email = request.POST.get('email')

        if email:
            if Subscriber.objects.filter(email=email).exists():
                messages.info(
                    request, 'You are already subscribed to our newsletter.'
                )
            else:
                try:
                    Subscriber.objects.create(email=email)
                    messages.success(
                        request,
                        'Thank you for subscribing to our newsletter!'
                    )
                except Exception as e:
                    messages.error(
                        request, 'Please enter a valid email address.'
                    )
        else:
            messages.error(request, 'Please enter a valid email address.')

        return redirect(request.META.get('HTTP_REFERER', '/'))


def unsubscribe(request):
    """Allow users to unsubscribe from the newsletter."""
    if request.method == 'POST':
        email = request.POST.get('email')

        if email:
            try:
                subscriber = Subscriber.objects.get(email=email)
                subscriber.delete()
                messages.success(
                    request,
                    'You have been successfully unsubscribed from our newsletter.'
                )
            except Subscriber.DoesNotExist:
                messages.error(
                    request,
                    'This email address was not found in our subscriber list.'
                )
        else:
            messages.error(request, 'Please enter a valid email address.')

        return redirect('newsletter:unsubscribe')

    return render(request, 'newsletter/unsubscribe.html')