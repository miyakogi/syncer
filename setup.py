#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from os import path

from setuptools import setup

readme_file = path.join(path.dirname(path.abspath(__file__)), 'README.rst')
with open(readme_file) as readme_file:
    readme = readme_file.read()

test_requirements = ['xfail']

setup(
    name='syncer',
    version='2.0.2',
    description='Async to sync converter',
    long_description=readme,
    author='Hiroyuki Takagi',
    author_email='miyako.dev@gmail.com',
    url='https://github.com/miyakogi/syncer',
    py_modules=['syncer'],
    include_package_data=True,
    license="MIT",
    zip_safe=False,
    keywords='syncer',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
    ],
    test_suite='tests',
    tests_require=test_requirements,

)
