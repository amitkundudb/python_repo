import unittest
from src.linear_algebra.utils import linearalgebra


class LinearAlgebraTest(unittest.TestCase):
    def test_one(self):
        self.assertEquals(linearalgebra(),0.0)
    '''2
1.1 1.1
1.1 1.1'''


    def test_two(self):
        self.assertEquals(linearalgebra(), 0.11)

    '''2
1.1 1.1
1.1 1.2'''
    def test_three(self):
        self.assertEquals(linearalgebra(), 6.0)
    '''3
1 2 3
4 5 6
1 2 1'''