from django.urls import path
from . import views

app_name = 'orders'

urlpatterns = [
    path('checkout/<int:package_id>/', views.checkout, name='checkout'),
    path('create-checkout-session/<int:package_id>/', views.create_checkout_session, name='create_checkout_session'),
    path('success/', views.success, name='success'),
    path('cancel/', views.cancel, name='cancel'),
]