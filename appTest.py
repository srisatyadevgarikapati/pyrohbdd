#!/usr/bin/env python
import unittest
class TestHello(unittest.TestCase):
        def setUp(self):
                self.assertEqual("h","hasas")
        def testPrintsTrue(self):
                self.assertTrue(True)
                
if __name__ == '__main__':
    unittest.main()
