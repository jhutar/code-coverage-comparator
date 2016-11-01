#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from setuptools import setup

def readme():
    with open('README.rst') as f:
        return f.read()

setup(name='cococo',
      version='0.1',
      description='COde COverage reports COmparator',
      long_description=readme(),
      classifiers=[
        'Development Status :: 1 - Planning',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        'Programming Language :: Python :: 2.7',
        'Topic :: Software Development',
      ],
      keywords='code-coverage diff',
      url='TODO',
      author='Jan Hutar',
      author_email='jhutar@redhat.com',
      license='GPLv3+',
      packages=['cococo'],
      install_requires=['tabulate', 'difflib', 'csv', 'json'],
      include_package_data=True,
      zip_safe=False)
