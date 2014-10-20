#!/usr/bin/env python2

import sys
import unittest
from tests.selenium_tests import SeleniumTestCase

if __name__ == '__main__':
    suite = unittest.TestSuite((
        unittest.makeSuite(SeleniumTestCase),
    ))
    result = unittest.TextTestRunner().run(suite)
    sys.exit(not result.wasSuccessful())
