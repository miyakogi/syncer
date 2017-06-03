#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from os import path

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

readme_file = path.join(path.dirname(path.abspath(__file__)), 'README.rst')
with open(readme_file) as readme_file:
    readme = readme_file.read()

install_requires = ['typing'] if sys.version_info < (3, 6) else []

setup(
    name='syncer',
    version='1.3.0',
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
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    test_suite='test_syncer',
    install_requires=install_requires,
)
