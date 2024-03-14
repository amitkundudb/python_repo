import unittest
from src.iterators_iterables.utils import iterables_iterators


class IteratorsTest(unittest.TestCase):
    def test_one(self):
        self.assertEquals(iterables_iterators(),0.833)
    '''4 
a a c d
2'''


    def test_two(self):
        self.assertEquals(iterables_iterators(), 0.722)

    '''9
a b c a d b z e o
4'''
    def test_three(self):
        self.assertEquals(iterables_iterators(), 0.881)
    '''9
a a a a d e u o i
3'''