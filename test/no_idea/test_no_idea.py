import unittest
from src.no_idea.utils import no_idea


class NoIdeaTest(unittest.TestCase):
    def test_one(self):
        self.assertEquals(no_idea(),1)
        '''3 2
1 5 3
3 1
5 7'''
    def test_two(self):
        self.assertEquals(no_idea(), 1)

    '''5 5
1 2 3 4 5
1 3 5 7 9
2 4 6 8 10'''

    def test_three(self):
        self.assertEquals(no_idea(),1)
    '''5 5
999999991 999999992 999999993 999999994 999999999
999999991 999999993 999999995 999999999 999999997
999999990 999999992 999999996 999999998 999999994'''