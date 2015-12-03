from cms.api import add_plugin, create_page, publish_page
from django.conf import settings
from django.contrib.auth.models import User
from django.test import TestCase
from django.test.client import Client
from django.test.utils import override_settings


def _setup_testing_env(self):
    # create a User
    self.testuser = User.objects.create_superuser('test',
                                                  'test@example.com',
                                                  'testpass')

    # Every test needs a client.
    self.page = create_page('Test Page', 'test.html', 'en', slug='/',
                            created_by=self.testuser)
    self.placeholder = self.page.placeholders.get(slot='slot')
    add_plugin(self.placeholder, 'MathJaxPlugin', 'en')
    publish_page(self.page, self.testuser, 'en')
    self.client = Client()
    self.response = self.client.get('/')
    self.content = str(self.response.content)
    return self


@override_settings(ROOT_URLCONF='tests.urls')
class RenderPluginTestCase(TestCase):
    urls = 'tests.urls'

    def setUp(self):
        # create a User
        self = _setup_testing_env(self)

    def test_simplemathjax(self):
        self.assertEqual(self.response.status_code, 200)
        self.assertIn(settings.MATHJAX_PATH[:15], self.content)
        self.assertNotIn('dontusesekizaicomment', self.content)


@override_settings(ROOT_URLCONF='tests.urls')
class MathJaxConfigurationTestCase(TestCase):
    urls = 'tests.urls'

    def setUp(self):
        self = _setup_testing_env(self)

    def test_all_configurations(self):
        for name in settings.MATHJAX_CONFIG_FILES:
            add_plugin(self.placeholder, 'MathJaxPlugin',
                       'en', config_file=name
                       )
            publish_page(self.page, self.testuser, 'en')
            self.response = self.client.get('/')
            self.content = str(self.response.content)
            self.assertIn(name, self.content)
        self.assertNotIn('dontusesekizaicomment', self.content)


@override_settings(ROOT_URLCONF='tests.urls', MATHJAX_USE_SEKIZAI=False)
class MathJaxConfigurationTestCase(TestCase):
    urls = 'tests.urls'

    def setUp(self):
        self = _setup_testing_env(self)

    def test_dontusesekizai(self):
        self.assertIn('dontusesekizaicomment', self.content)

    def test_all_configurations(self):
        for name in settings.MATHJAX_CONFIG_FILES:
            add_plugin(self.placeholder, 'MathJaxPlugin',
                       'en', config_file=name
                       )
            publish_page(self.page, self.testuser, 'en')
            self.response = self.client.get('/')
            self.content = str(self.response.content)
            self.assertIn(name, self.content)


DefaultConfigData = '''
Here should be javascript code. But it is just a test.
'''
SampleConfidData = '''
Here should be javascript code. But it is absent yet.
'''


@override_settings(ROOT_URLCONF='tests.urls',
                   MATHJAX_DEFAULT_CONFIG=DefaultConfigData,
                   MATHJAX_USE_SEKIZAI=False)
class MathJaxDefaultConfigTestCase(TestCase):
    urls = 'tests.urls'

    def setUp(self):
        self = _setup_testing_env(self)

    def test_is_defaults_loaded(self):
        self.assertIn(DefaultConfigData, self.content)

    def test_defaults_and_extra(self):
        add_plugin(self.placeholder, 'MathJaxPlugin',
                   'en', config_data=SampleConfidData
                   )
        publish_page(self.page, self.testuser, 'en')
        self.response = self.client.get('/')
        self.content = str(self.response.content)
        self.assertIn(SampleConfidData, self.content)


# Default configs without sekizai
@override_settings(ROOT_URLCONF='tests.urls',
                   MATHJAX_DEFAULT_CONFIG=DefaultConfigData
                   )
class DefaultConfig_WO_SekizaiTestCase(TestCase):
    urls = 'tests.urls'

    def setUp(self):
        self = _setup_testing_env(self)

    def test_is_defaults_loaded(self):
        self.assertIn(DefaultConfigData, self.content)

    def test_defaults_and_extra(self):
        add_plugin(self.placeholder, 'MathJaxPlugin',
                   'en',
                   config_data=SampleConfidData
                   )
        publish_page(self.page, self.testuser, 'en')
        self.response = self.client.get('/')
        self.content = str(self.response.content)
        self.assertIn(SampleConfidData, self.content)
