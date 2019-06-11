from django.contrib import admin

from core.models import Website


@admin.register(Website)
class WebsiteAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'url', 'status', 'status_changed')
    list_display_links = ('id', 'name', 'url')
    fields = ('name', 'url', 'status', 'status_changed')
    readonly_fields = ('status', 'status_changed')
