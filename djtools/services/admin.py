from django.contrib import admin

from .models import Service


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'active',
        'featured',
        'order',
    ]

    list_filter = [
        'active',
        'featured',
    ]

    prepopulated_fields = {
        'slug': ('title',)
    }
