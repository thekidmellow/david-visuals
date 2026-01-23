from django.contrib import admin
from .models import Hero


@admin.register(Hero)
class HeroAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_active', 'created_at')
    list_filter = ('is_active', 'created_at')
    search_fields = ('title', 'subtitle', 'description')
    list_editable = ('is_active',)
    ordering = ('-created_at',)
