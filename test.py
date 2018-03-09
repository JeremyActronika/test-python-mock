#!/usr/bin/env python3
import unittest
from mock import MagicMock
import sys


sys.modules['toto'] = MagicMock()

tests = unittest.TestLoader().discover('.', '*_test.py')
testRunner = unittest.runner.TextTestRunner(verbosity=2)
ret = not testRunner.run(tests).wasSuccessful()
sys.exit(ret)
