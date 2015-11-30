
from cms.models.pluginmodel import CMSPlugin
from cms.plugin_base import CMSPluginBase
from django.conf import settings
from .models import MathJaxConfig


class InsertMathJax(CMSPluginBase):
    model = CMSPlugin
    name = "MathJax sources"
    render_template = "cms/plugins/mathjax.html"

    def render(self, context, instance, placeholder):

        context.update({
            'mathjax': getattr(settings, 'MATHJAXPATH', '//cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML')
                        })
        return context

    
plugin_pool.register_plugin(InsertMathJax)