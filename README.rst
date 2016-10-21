.. image:: https://badge.fury.io/py/cmsplugin-mathjax.svg
	   :target: https://badge.fury.io/py/cmsplugin-mathjax

.. image:: https://img.shields.io/pypi/dm/cmsplugin-mathjax.svg
	   :target: https://pypi.python.org/pypi/cmsplugin-mathjax

.. image:: https://img.shields.io/pypi/status/cmsplugin-mathjax.svg
	   :target: https://pypi.python.org/pypi/cmsplugin-mathjax

.. image:: https://img.shields.io/pypi/pyversions/cmsplugin-mathjax.svg
	   :target: https://pypi.python.org/pypi/cmsplugin-mathjax

.. image:: https://img.shields.io/pypi/l/cmsplugin-mathjax.svg
	   :target: https://raw.githubusercontent.com/FabriceSalvaire/cmsplugin-mathjax/master/LICENSE.txt

=========================
Django CMS MathJax Plugin
=========================

`Django CMS <https://www.django-cms.org>`_ MathJax Plugin provides a plugin that allows you to use `MathJax <https://www.mathjax.org/>`_ markups within a page.

This plugin was rewritten from a prior work of Dmitry E. Kislov in late 2015 (cf. forked repo).

Despite it works fine, it isn't a very elegant solution since it doesn't add content but add javascript ressource to the page instead.

Note we don't need a plugin for MathJax contents since MathJax acts as a parser and don't relies on classes.

Installation
------------

This plugin requires django CMS 3 or higher to be properly installed.

* Within your ``virtualenv`` run ``pip install cmsplugin-mathjax``
* Check you have ``'django_sekizai'`` in your ``INSTALLED_APPS`` setting
* Add ``'cmsplugin_mathjax'`` to your ``INSTALLED_APPS`` setting
* Run ``manage.py migrate cmsplugin_mathjax``

Usage
-----

You just have to add this plugin in your page structure somewhere (best at the beginning).
