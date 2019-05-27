import unittest
from .pypiproject_core import *

class TestCoreModule(unittest.TestCase):

    currentResult = None # holds last result object passed to run method

    def setUp(self):
        pass

    def tearDown(self):
        ok = self.currentResult.wasSuccessful()
        errors = self.currentResult.errors
        failures = self.currentResult.failures
        print ('All tests passed so far!' if ok else \
                ' %d errors and %d failures so far' % \
                (len(errors), len(failures)))

    def run(self, result=None):
        self.currentResult = result # remember result for use in tearDown
        unittest.TestCase.run(self, result) # call superclass run method

    def test_input(self):
        self.assertEqual(getText("test text"), "test text")

    def test_output(self):
        self.assertEqual(getText("test text", "string"), "test text")
        self.assertEqual(getText("test text", "json"), {"text": "test text"})


def runUnittests():
    suite = unittest.TestSuite()
    for method in dir(TestCoreModule):
       if method.startswith("test"):
          suite.addTest(TestCoreModule(method))
    return unittest.TextTestRunner(verbosity=3).run(suite)

#testCase = TestCoreModule() 

#suite = unittest.TestLoader().loadTestsFromModule (TestCoreModule())
#unittest.TextTestRunner(verbosity=3).run(suite)

#if __name__ == 'pypiproject.core.pypiproject_core_unittest':
    #unittest.main()
    
