from django.shortcuts import redirect
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
