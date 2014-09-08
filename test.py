import sys
import django
from django.conf import settings

settings.configure(
    DEBUG = True,
    DATABASES = {
            'default': {
            'ENGINE': 'django.db.backends.sqlite3',
        }
    },
    INSTALLED_APPS = (
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'shopify_sync',
    ),
    MIDDLEWARE_CLASSES = ()
)

django.setup()

from django.test.runner import DiscoverRunner

test_runner = DiscoverRunner()
failures = test_runner.run_tests(['shopify_sync'])
if failures:
    sys.exit(failures)
