#!/usr/bin/env python
import unittest
class TestHello(unittest.TestCase):
        def setUp(self):
                self.assertEqual("h","hasas")
                with self.assertRaises(TypeError):
if __name__ == '__main__':
    unittest.main()
