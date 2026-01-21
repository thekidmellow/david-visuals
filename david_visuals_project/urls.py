from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.sitemaps.views import sitemap
from sitemaps import StaticViewSitemap, PackageSitemap

sitemaps = {
    'static': StaticViewSitemap,
    'packages': PackageSitemap,
}

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    path('', include('home.urls')),
    path('packages/', include('packages.urls')),
    path('profile/', include('profiles.urls')),
    path('orders/', include('orders.urls')),
    path('newsletter/', include('newsletter.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = 'django.views.defaults.page_not_found'