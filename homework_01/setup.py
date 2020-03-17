import os
from setuptools import setup

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='otus_hw_01',
    version='0.1',
    packages=['search'],
    include_package_data=True,
    license='GNU General Public License v3.0',
    description='homework with search',
    # long_description=README,
    url='https://github.com/ivan985/learning',
    author='Ivan Nikitin',
    author_email='hikitiniv@leninka.com',
    keywords=['web', 'search'],
    classifiers=[],
)
