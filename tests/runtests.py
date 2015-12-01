import os
import sys

import django
from django.conf import settings
from django.core.management import call_command
from django.test.utils import get_runner


if __name__ == "__main__":
    os.environ['DJANGO_SETTINGS_MODULE'] = 'tests.test_settings'
    django.setup()
    call_command('makemigrations','cmsplugin_mathjax')
    TestRunner = get_runner(settings)
    test_runner = TestRunner()
    failures = test_runner.run_tests(["tests.tests"])
    sys.exit(bool(failures))
