#!/usr/bin/env python
import unittest


class TestHello(unittest.TestCase):
        def setUp(self):
                self.assertEqual("Softlayer","Softlayer")
        def testPrintsTrue(self):
                self.assertTrue(True)
                
if __name__ == '__main__':
    unittest.main()


