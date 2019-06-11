from django.db import models
from django.utils.translation import ugettext_lazy as _
from model_utils import Choices
from model_utils.models import StatusModel


class Website(StatusModel):
    STATUS = Choices(
        '0',
        '200',
        '400', '401', '403', '404',
        '500', '502', '503', '504')
    name = models.CharField(
        max_length=100,
        verbose_name=_('Website Name')
    )
    url = models.URLField(
        verbose_name=_('URL')
    )

    class Meta:
        verbose_name = _('Website')
        verbose_name_plural = _('Websites')

    def __str__(self):
        return self.name
