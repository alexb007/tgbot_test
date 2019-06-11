from django.contrib import admin

from core.models import Crypto


@admin.register(Crypto)
class CryptoAdmin(admin.ModelAdmin):
    fields = ('name', 'current_rate', 'rate_changed')
    readonly_fields = ('current_rate', 'rate_changed')
