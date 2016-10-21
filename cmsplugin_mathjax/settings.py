####################################################################################################

from django.conf import settings

####################################################################################################

# Default MathJax CDN URL
# https://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-MML-AM_CHTML
MATHJAX_URL = getattr(settings, 'MATHJAX_URL', 'https://cdn.mathjax.org/mathjax/latest/MathJax.js')

# Default inline configuration passed to MathJax
# http://docs.mathjax.org/en/latest/configuration.html#loading
MATHJAX_INLINE_CONFIG = getattr(settings, 'MATHJAX_INLINE_CONFIG', None)

# http://docs.mathjax.org/en/latest/config-files.html#common-configurations
MATHJAX_CONFIG_FILES = [
    'default',

    'TeX-MML-AM_CHTML',
# MathJax.Hub.Config({
#   jax: ["input/TeX","input/MathML","input/AsciiMath","output/CommonHTML"],
#   extensions: ["tex2jax.js","mml2jax.js","asciimath2jax.js","MathMenu.js","MathZoom.js","AssistiveMML.js", "[Contrib]/a11y/accessibility-menu.js"],
#   TeX: {
#     extensions: ["AMSmath.js","AMSsymbols.js","noErrors.js","noUndefined.js"]
#   }
# });

    'TeX-MML-AM_HTMLorMML',
# MathJax.Hub.Config({
#   config: ["MMLorHTML.js"],
#   jax: ["input/TeX","input/MathML","input/AsciiMath","output/HTML-CSS","output/NativeMML", "output/PreviewHTML"],
#   extensions: ["tex2jax.js","mml2jax.js","asciimath2jax.js","MathMenu.js","MathZoom.js", "fast-preview.js", "AssistiveMML.js", "[Contrib]/a11y/accessibility-menu.js"],
#   TeX: {
#     extensions: ["AMSmath.js","AMSsymbols.js","noErrors.js","noUndefined.js"]
#   }
# });

    'TeX-MML-AM_SVG',
# MathJax.Hub.Config({
#   jax: ["input/TeX","input/MathML","input/AsciiMath","output/HTML-CSS","output/NativeMML", "output/PreviewHTML"],
#   extensions: ["tex2jax.js","mml2jax.js","asciimath2jax.js","MathMenu.js","MathZoom.js", "fast-preview.js", "AssistiveMML.js", "[Contrib]/a11y/accessibility-menu.js"],
#   TeX: {
#     extensions: ["AMSmath.js","AMSsymbols.js","noErrors.js","noUndefined.js"]
#   }
# });

    'TeX-AMS-MML_HTMLorMML',
# MathJax.Hub.Config({
#   config: ["MMLorHTML.js"],
#   jax: ["input/TeX","input/MathML","output/HTML-CSS","output/NativeMML", "output/PreviewHTML"],
#   extensions: ["tex2jax.js","mml2jax.js","MathMenu.js","MathZoom.js", "fast-preview.js", "AssistiveMML.js", "[Contrib]/a11y/accessibility-menu.js"],
#   TeX: {
#     extensions: ["AMSmath.js","AMSsymbols.js","noErrors.js","noUndefined.js"]
#   }
# });

    'TeX-AMS_CHTML',
# MathJax.Hub.Config({
#   jax: ["input/TeX","output/CommonHTML"],
#   extensions: ["tex2jax.js","MathMenu.js","MathZoom.js", "AssistiveMML.js", "[Contrib]/a11y/accessibility-menu.js"],
#   TeX: {
#     extensions: ["AMSmath.js","AMSsymbols.js","noErrors.js","noUndefined.js"]
#   }
# });

    'TeX-AMS_SVG',
# MathJax.Hub.Config({
#   jax: ["input/TeX","output/SVG", "output/PreviewHTML"],
#   extensions: ["tex2jax.js","MathMenu.js","MathZoom.js", "fast-preview.js", "AssistiveMML.js", "[Contrib]/a11y/accessibility-menu.js"],
#   TeX: {
#     extensions: ["AMSmath.js","AMSsymbols.js","noErrors.js","noUndefined.js"]
#   }
# });

    'TeX-AMS_HTML',
# MathJax.Hub.Config({
#   jax: ["input/TeX","output/HTML-CSS", "output/PreviewHTML"],
#   extensions: ["tex2jax.js","MathMenu.js","MathZoom.js", "fast-preview.js", "AssistiveMML.js", "[Contrib]/a11y/accessibility-menu.js"],
#   TeX: {
#     extensions: ["AMSmath.js","AMSsymbols.js","noErrors.js","noUndefined.js"]
#   }
# });

    'MML_CHTML',
# MathJax.Hub.Config({
#   jax: ["input/MathML", "output/CommonHTML"],
#   extensions: ["mml2jax.js","MathMenu.js","MathZoom.js", "AssistiveMML.js", "[Contrib]/a11y/accessibility-menu.js"]
# });

    'MML_SVG',
# MathJax.Hub.Config({
#   jax: ["input/MathML","output/SVG", "output/PreviewHTML"],
#   extensions: ["mml2jax.js","MathMenu.js","MathZoom.js", "fast-preview.js", "AssistiveMML.js", "[Contrib]/a11y/accessibility-menu.js"]
# });

    'MML_HTMLorMML',
# MathJax.Hub.Config({
#   config: ["MMLorHTML.js"],
#   jax: ["input/MathML","output/HTML-CSS","output/NativeMML", "output/PreviewHTML"],
#   extensions: ["mml2jax.js","MathMenu.js","MathZoom.js", "fast-preview.js", "AssistiveMML.js", "[Contrib]/a11y/accessibility-menu.js"]
# });

    'AM_CHTML',
# MathJax.Hub.Config({
#   jax: ["input/AsciiMath","output/CommonHTML"],
#   extensions: ["asciimath2jax.js","MathMenu.js","MathZoom.js","AssistiveMML.js", "[Contrib]/a11y/accessibility-menu.js"]
# });

    'AM_SVG',
# MathJax.Hub.Config({
#   config: ["MMLorHTML.js"],
#   jax: ["input/AsciiMath","output/SVG", "output/PreviewHTML",
#   extensions: ["asciimath2jax.js","MathMenu.js","MathZoom.js", "fast-preview.js","AssistiveMML.js", "[Contrib]/a11y/accessibility-menu.js"]
# });

    'AM_HTMLorMML',
# MathJax.Hub.Config({
#   config: ["MMLorHTML.js"],
#   jax: ["input/AsciiMath","output/HTML-CSS","output/NativeMML", "output/PreviewHTML"],
#   extensions: ["asciimath2jax.js","MathMenu.js","MathZoom.js", "fast-preview.js", "AssistiveMML.js", "[Contrib]/a11y/accessibility-menu.js"]
# });

    'TeX-AMS-MML_SVG',
# MathJax.Hub.Config({
#   jax: ["input/TeX","input/MathML","output/SVG", "output/PreviewHTML"],
#   extensions: ["tex2jax.js","mml2jax.js","MathMenu.js","MathZoom.js", "fast-preview.js", "AssistiveMML.js", "[Contrib]/a11y/accessibility-menu.js"],
#   TeX: {
#     extensions: ["AMSmath.js","AMSsymbols.js","noErrors.js","noUndefined.js"]
#   }
# });
]
