import os, sys
from django.conf import settings

settings.configure(
    DEBUG = True,
    DATABASES = {
            'default': {
            'ENGINE': 'django.db.backends.sqlite3',
        }
    },
    #ROOT_URLCONF = 'shopify_webhook.urls',
    INSTALLED_APPS = (
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'shopify_sync',
    ),
)

from django.test.runner import DiscoverRunner

test_runner = DiscoverRunner(verbosity = 3)
failures = test_runner.run_tests(['shopify_sync'])
if failures:
    sys.exit(failures)