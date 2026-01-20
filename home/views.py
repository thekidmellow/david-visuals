from django.shortcuts import render
from .models import Hero


def index(request):
    hero = Hero.objects.filter(is_active=True).first()
    context = {
        'hero': hero,
    }
    return render(request, 'home/index.html', context)