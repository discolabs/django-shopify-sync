from distutils.core import setup

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

    packages = ['shopify_sync'],
    package_dir = {
        'shopify_sync': 'shopify_sync',
    },

    requires = [
        'django',
        'shopify',
        'owned_models',
        'jsonfield',
    ],

    install_requires = [
        'django',
    ],

    zip_safe=True,
    classifiers=[],
)

