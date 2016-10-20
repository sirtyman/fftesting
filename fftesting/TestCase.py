__author__ = 'Marcin'


import unittest
import fftesting.HTMLTestRunner as HTMLTestRunner


class TestCase(unittest.TestCase):
    pass



class Test1(TestCase):
    def test_1(self):
        self.assertTrue(1==1)



if __name__ == '__main__':
    unittest.main(testRunner=HTMLTestRunner.HTMLTestRunner).runTests()