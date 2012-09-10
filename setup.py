##############################################################################
#
# Copyright (c) 2011, 2012 Wapolabs
# All Rights Reserved.
#
##############################################################################
from setuptools import setup, find_packages
import sys, os

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.md')).read()
CHANGES = open(os.path.join(here, 'CHANGES.md')).read()

version='0.1.1'

setup(name='wapo-pyramid',
      version=version,
      description="Pyramid utilities for RESTful apps.",
      long_description="""\
""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='',
      author='',
      author_email='',
      url='',
      license='',
      namespace_packages = ['wapo'],
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
        "pyramid >= 1.3.2"
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
