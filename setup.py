from setuptools import setup

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

    packages = [
        'shopify_sync'
    ],

    package_dir = {
        'shopify_sync': 'shopify_sync',
    },

    install_requires = [
        'django >=1.6.5, <1.7',
        'django-owned-models >=0.0.4',
        'ShopifyAPI >=2.1.0',
        'jsonfield >=0.9.22',
    ],

    zip_safe=True,
    classifiers=[],
)