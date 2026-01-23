from django.shortcuts import render
from .models import Hero
from django.http import HttpResponse


def index(request):
    hero = Hero.objects.filter(is_active=True).first()
    context = {
        'hero': hero,
    }
    return render(request, 'home/index.html', context)


def robots_txt(request):
    lines = [
        "User-agent: *",
        "Disallow: /admin/",
        "Disallow: /accounts/",
        "Disallow: /profile/",
        "Disallow: /orders/",
        "Allow: /",
        "",
        f"Sitemap: {request.scheme}://{request.get_host()}/sitemap.xml",
    ]
    return HttpResponse("\n".join(lines), content_type="text/plain")
