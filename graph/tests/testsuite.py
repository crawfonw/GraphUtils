'''
Created on Dec 27, 2013

@author: Nick Crawford
'''

import unittest

if __name__ == '__main__':
    test_classes = []
    suites = map(unittest.TestLoader().loadTestsFromTestCase, test_classes)
    alltests = unittest.TestSuite(suites)
    unittest.TextTestRunner(verbosity=1).run(alltests)