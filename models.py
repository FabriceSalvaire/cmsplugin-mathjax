

from cms.models.pluginmodel import CMSPlugin
from django.conf import settings
from django.db import models
from django.utils.translation import ugettext_lazy as _


class MathJaxConfig(CMSPlugin):
    config_file = models.FileField(upload_to=settings.MATHJAX_UPLOADTO,
                                   verbose_name=_("Config file"),
                                   blank=True,
                                   null=True
                                   )
    config_data = models.TextField(verbose_name=_("Config data"), blank=True,
                                   default=True
                                   )