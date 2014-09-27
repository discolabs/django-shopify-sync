from setuptools import setup, find_packages

version = __import__('shopify_sync').__version__

setup(
    name = 'django-shopify-sync',
    version = version,
    description = 'A package for synchronising Django models with Shopify resources.',
    long_description = open('README.rst').read(),
    author = 'Gavin Ballard',
    author_email = 'gavin@gavinballard.com',
    url = 'https://github.com/gavinballard/django-shopify-sync',
    license = 'MIT',

    packages = find_packages(),

    install_requires = [
        'django >=1.7',
        'django-owned-models >=0.1.1',
        'django-shopify-webhook >=0.2.5',
        'ShopifyAPI >=2.1.0',
        'jsonfield >=0.9.22',
    ],

    tests_require = [
        'model_mommy >=1.2.1',
    ],

    zip_safe=True,
    classifiers=[],
)
