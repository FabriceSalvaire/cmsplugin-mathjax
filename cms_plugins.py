
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

    def render(self, context, instance, placeholder):

        context.update({
            'mathjax': getattr(settings, 'MATHJAX_PATH', '//cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML')
                        })
        return context


plugin_pool.register_plugin(MathJaxPlugin)
