
import unittest

from PROJECT_NAME.main import hello

class TestHelloWorld(unittest.TestCase):

    def test_hello(self):
        self.assertEqual(hello('World'), 'Hello, World')

