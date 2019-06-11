from django.db import models
from django.utils.translation import ugettext_lazy as _
from model_utils.fields import MonitorField


class Crypto(models.Model):
    name = models.CharField(
        max_length=10,
        verbose_name=_('Currency Name')
    )
    current_rate = models.FloatField(
        null=True,
        blank=True,
        editable=False,
        verbose_name=_('Current Rate')
    )
    rate_changed = MonitorField(
        monitor='current_rate',
        verbose_name=_('Last Rate Update')
    )

    class Meta:
        verbose_name = _('Crypto Currency')
        verbose_name_plural = _('Crypto Currencies')

    def __str__(self):
        return self.name
