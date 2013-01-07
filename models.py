from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.conf import settings
from cms.models import CMSPlugin

def _get_choices():
    choices = getattr(settings, 'CMSPLUGIN_SUBPAGES_TEMPLATES', None)
    return choices or  (
        ('default.html', _('Default')),
        )

class SubPage(CMSPlugin):
    ORDER_ASC = 0
    ORDER_DESC = 1

    ORDER_DIR_CHOICES = (
        (ORDER_ASC, _('Ascending')),
        (ORDER_DESC, _('Descending')),
    )

    ORDER_CREATION_DATE = 'creation_date'
    ORDER_CHANGED_DATE = 'changed_date'
    ORDER_PUBLICATION_DATE = 'publication_date'

    ORDER_CHOICES = (
        (ORDER_CREATION_DATE, _('Creation date')),
        (ORDER_CHANGED_DATE, _('Changed date')),
        (ORDER_PUBLICATION_DATE,  _('publication_date')),
    )

    amount_pages = models.PositiveIntegerField(default=10, verbose_name=_('Amount pages to show'))
    template = models.CharField(choices=_get_choices(), max_length=255)
    order_by = models.CharField(choices=ORDER_CHOICES, max_length=255, default=ORDER_CREATION_DATE)
    order_dir = models.PositiveSmallIntegerField(default=ORDER_ASC, choices=ORDER_DIR_CHOICES)


