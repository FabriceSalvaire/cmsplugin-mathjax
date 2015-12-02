
# Default configuration passed to MathJax
MATHJAX_DEFAULT_CONFIG = None

# MathJax default source file name
MATHJAX_JS = 'MathJax.js'

# Default MathJax CDN-path
MATHJAX_PATH = '//cdn.mathjax.org/mathjax/latest/'

# if True MathJax will use django-sekizai,
# otherwise it will insert js-sources in-place.
MATHJAX_USE_SEKIZAI = True

# Presets for MathJax v. 2.6
MATHJAX_CONFIG_FILES = ['TeX-AMS-MML_HTMLorMML',
                      'TeX-AMS_HTML',
                      'MML_HTMLorMML',
                      'AM_HTMLorMML',
                      'TeX-AMS-MML_SVG',
                      'TeX-MML-AM_HTMLorMML'
                      ]
