from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import UserProfile
from .forms import UserProfileForm
from orders.models import Order


@login_required
def profile(request):
    profile = request.user.profile
    
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully!')
            return redirect('profile')
    else:
        form = UserProfileForm(instance=profile)
    
    context = {
        'form': form,
        'profile': profile,
    }
    return render(request, 'profiles/profile.html', context)


@login_required
def order_history(request):
    orders = Order.objects.filter(user=request.user).select_related('package')
    
    context = {
        'orders': orders,
    }
    return render(request, 'profiles/order_history.html', context)