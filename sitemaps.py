from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from packages.models import Package


class StaticViewSitemap(Sitemap):
    priority = 0.8
    changefreq = 'monthly'

    def items(self):
        return ['home:index', 'packages:package_list']

    def location(self, item):
        return reverse(item)


class PackageSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.9

    def items(self):
        return Package.objects.filter(is_active=True)

    def lastmod(self, obj):
        return obj.updated_at

    def location(self, obj):
        return reverse('packages:package_detail', args=[obj.pk])