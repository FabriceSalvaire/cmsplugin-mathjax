
from cms.models.pluginmodel import CMSPlugin
from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from .models import MathJaxConfig


class MathJaxPlugin(CMSPluginBase):
    model = MathJaxConfig
    name = _("Insert MathJax Sources")
    render_template = "cms/plugins/mathjax.html"
    text_enabled = False

    def render(self, context, instance, placeholder):
        mathjax = settings.MATHJAX_PATH + settings.MATHJAX_JS
        defaults = settings.MATHJAX_DEFAULT_CONFIG
        if instance.config_file:
            mathjax += '?config=' + instance.config_file
        context.update({
            'mathjax': mathjax,
            'use_sekizai': settings.MATHJAX_USE_SEKIZAI,
            'config_data': instance.config_data,
            'default_config': defaults
                        })
        return context


plugin_pool.register_plugin(MathJaxPlugin)
