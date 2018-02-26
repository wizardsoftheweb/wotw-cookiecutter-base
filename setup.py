"""This file sets up the package"""

from setuptools import setup

with open('VERSION') as version_file:
    __version__ = version_file.read().strip()

setup(
    name='wotw-cookiecutter-base',
    version=__version__,
    packages=[],
    package_data={
        '': [
            'VERSION',
        ]
    },
    include_package_data=True
)
