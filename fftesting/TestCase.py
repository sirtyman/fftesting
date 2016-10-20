__author__ = 'Marcin'


import unittest
import fftesting.HTMLTestRunner as HTMLTestRunner


class TestCase(unittest.TestCase):
    pass



class Test1(TestCase):
    def test_1(self):
        TestCase.assertTrue(True)



if __name__ == '__main__':
    unittest.main(testRunner=HTMLTestRunner).runTests()