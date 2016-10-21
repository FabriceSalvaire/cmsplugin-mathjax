####################################################################################################

from django.db import models
from django.utils.translation import ugettext_lazy as _

from cms.models.pluginmodel import CMSPlugin

from . import settings

####################################################################################################

class MathJaxConfig(CMSPlugin):

    CHOICES = [(x, x) for x in settings.MATHJAX_CONFIG_FILES]

    config_file = models.CharField(
        verbose_name=_('Configuration File'),
        choices=CHOICES,
        max_length=25,
        blank=True,
        default='TeX-MML-AM_CHTML',
        help_text=_('see <a href="http://docs.mathjax.org/en/latest/config-files.html#common-configurations" target="_blank">Mathjax Doc</a>'),
    )

    inline_config = models.TextField(
        verbose_name=_("Inline Configuration"),
        blank=True,
        default='', # settings.inline_config
        help_text=_('javascript code, see <a href="http://docs.mathjax.org/en/latest/configuration.html#loading" target="_blank">Mathjax Doc</a>'),
    )
