#!/usr/bin/env python
"""

test - Run all or a specific test

"""
import os, sys, unittest, Hellanzb.test
from Hellanzb.Core import init

TEST_DIR = os.path.join(os.path.dirname(__file__), 'Hellanzb/test/')

def suite(testName = None):
    s = unittest.TestSuite()
    for file in os.listdir(TEST_DIR):
        if file.endswith('TestCase.py') and not file.startswith('.') and \
                (not testName or file.startswith(testName)):
            packageName = file[:-3]
            module = __import__('Hellanzb.test.' + packageName, globals(), locals(), packageName)
            klass = getattr(module, packageName)
            if klass.skip:
                print 'Skipping test: %s' % packageName
            else:
                print 'Loading test: %s' % packageName
                s.addTest(unittest.makeSuite(klass, 'test'))
    return s

if __name__ == '__main__':
    Hellanzb.Core.init()
    try:
        if len(sys.argv) > 1:
            unittest.TextTestRunner().run(suite(sys.argv[1]))
        else:
            unittest.TextTestRunner().run(suite())
    finally:
        Hellanzb.Core.shutdown()
