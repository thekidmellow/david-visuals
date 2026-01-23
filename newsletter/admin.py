from django.contrib import admin
from .models import Subscriber


@admin.register(Subscriber)
class SubscriberAdmin(admin.ModelAdmin):
    list_display = ('email', 'subscribed_at', 'is_active')
    list_filter = ('is_active', 'subscribed_at')
    search_fields = ('email',)
    list_editable = ('is_active',)
    readonly_fields = ('subscribed_at',)
    ordering = ('-subscribed_at',)
