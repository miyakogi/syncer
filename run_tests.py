#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import unittest

tests = ['test_syncer_py34.py']
if sys.version_info >= (3, 5):
    pattern = 'test*.py'
else:
    pattern = 'test*py34.py'

tests = unittest.defaultTestLoader.discover(start_dir='.', pattern=pattern)
runner = unittest.TextTestRunner()
runner.run(tests)
