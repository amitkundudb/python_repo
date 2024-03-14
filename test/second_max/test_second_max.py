import unittest
from src.second_max.utils import find_second_most_number


class SecondMostTest(unittest.TestCase):
    def test_one(self):
        self.assertEquals(find_second_most_number(),5)
        '''5
2 3 6 6 5'''
    def test_two(self):
        self.assertEquals(find_second_most_number(),-57 )

    '''4
57 57 -57 57'''

    def test_three(self):
        self.assertEquals(find_second_most_number(),89)
    '''4
29 90 43 89'''