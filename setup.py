"""
Django git backend - the git storage backend

This thing stores your files in git. That way your files are automatically
deduplicated.
"""
from setuptools import setup, find_packages


__version__ = "0.0.1"


setup(
    # package name in pypi
    name='django-dedupe-backend',
    # extract version from module.
    version=__version__,
    description="The super storage backend",
    long_description=__doc__,
    classifiers=[],
    keywords='django storage backend that stores files in git',
    author='Lars van de Kerkhof',
    author_email='lars@permanentmarkers.nl',
    url='',
    license='',
    # include all packages in the egg, except the test package.
    packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
    # for avoiding conflict have one namespace for all apc related eggs.
    namespace_packages=[],
    # include non python files
    include_package_data=True,
    zip_safe=False,
    # specify dependencies
    install_requires=[
        'setuptools',
    ],
    # mark test target to require extras.
    extras_require = {
        'test':  ["mock"]
    },
)
