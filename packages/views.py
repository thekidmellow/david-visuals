from django.shortcuts import render, get_object_or_404
from .models import Package


def package_list(request):
    packages = Package.objects.filter(is_active=True)
    category = request.GET.get('category')
    
    if category:
        packages = packages.filter(category=category)
    
    context = {
        'packages': packages,
        'selected_category': category,
    }
    return render(request, 'packages/package_list.html', context)


def package_detail(request, pk):
    package = get_object_or_404(Package, pk=pk, is_active=True)
    context = {
        'package': package,
    }
    return render(request, 'packages/package_detail.html', context)