#!/usr/bin/env python2

import sys
import unittest
from tests.selenium_tests import SeleniumTestsCase

if __name__ == '__main__':
    suite = unittest.TestSuite((
        unittest.makeSuite(SeleniumTestsCase),
    ))
    result = unittest.TextTestRunner().run(suite)
    sys.exit(not result.wasSuccessful())
