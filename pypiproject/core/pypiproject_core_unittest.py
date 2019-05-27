import unittest
from .pypiproject_core import *

class TestCoreModule(unittest.TestCase):
    def test_input(self):
        self.assertEqual(getText("test text"), "test text")

    def test_output(self):
        self.assertEqual(getText("test text", "string"), "test text")
        self.assertEqual(getText("test text", "json"), {"text": "test text"})


#if __name__ == '__main__':
unittest.main()