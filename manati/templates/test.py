
import unittest

from PROJECT_NAME.MODULE_NAME import hello

class TestHelloWorld(unittest.TestCase):

    def test_hello(self):
        self.assertEqual(hello('World'), 'Hello, World')

