from django.contrib import admin
from .models import Order


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = (
        'order_number', 'user', 'package', 'total', 'status', 'created_at'
    )
    list_filter = ('status', 'created_at')
    search_fields = (
        'order_number', 'user__username', 'user__email', 'stripe_pid'
    )
    list_editable = ('status',)
    readonly_fields = (
        'order_number', 'created_at', 'updated_at', 'stripe_pid'
    )
    ordering = ('-created_at',)

    fieldsets = (
        ('Order Information', {
            'fields': ('order_number', 'user', 'package', 'total', 'status')
        }),
        ('Payment Information', {
            'fields': ('stripe_pid',)
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at')
        }),
    )
