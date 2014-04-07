from distutils.core import setup

version=__import__('shopify_sync').__version__

setup(
    name='django-shopify-sync',
    version=version,
    description='A package for synchronising Django models with Shopify resources.',
    long_description=open('README.rst').read(),
    author='Gavin Ballard',
    author_email='gavin@gavinballard.com',
    url='https://github.com/gavinballard/django-shopify-sync',
    license='MIT',

    packages=['shopify_sync'],
    package_dir={
        'shopify_sync': 'shopify_sync',
    },

    requires=['Django (>=1.3)',],
    install_requires=['Django>=1.3',],

    zip_safe=True,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
