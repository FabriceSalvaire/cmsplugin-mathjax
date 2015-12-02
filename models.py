

from cms.models.pluginmodel import CMSPlugin
from django.conf import settings
from django.db import models
from django.utils.translation import ugettext_lazy as _


class MathJaxConfig(CMSPlugin):
    CHOICES = [(x, x) for x in settings.MATHJAX_CONFIG_FILES]
    config_file = models.CharField(blank=True,
                                   verbose_name=_('Configuration preset'),
                                   choices=CHOICES,
                                   max_length=100
                                   )
    config_data = models.TextField(verbose_name=_("Configuration data"),
                                   blank=True,
                                   default=''
                                   )
