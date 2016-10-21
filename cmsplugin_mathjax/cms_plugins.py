####################################################################################################

from django.utils.translation import ugettext_lazy as _

from cms.models.pluginmodel import CMSPlugin
from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from .models import MathJaxConfig
from . import settings

####################################################################################################

class MathJaxPlugin(CMSPluginBase):

    model = MathJaxConfig
    name = _("Enable MathJax on the page")
    render_template = "cmsplugin_mathjax/plugin.html"

    ##############################################

    def render(self, context, instance, placeholder):

        mathjax_url = settings.MATHJAX_URL
        if instance.config_file:
            mathjax_url += '?config=' + instance.config_file
        if instance.inline_config:
            inline_config = instance.inline_config
        else:
            inline_config = settings.MATHJAX_INLINE_CONFIG
        context.update({
            'mathjax_url': mathjax_url,
            'inline_config': inline_config,
        })

        return context

####################################################################################################

plugin_pool.register_plugin(MathJaxPlugin)
