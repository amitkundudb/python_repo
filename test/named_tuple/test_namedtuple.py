import unittest
from src.named_tuple.utils import named_tuple


class TupleTest(unittest.TestCase):
    def test_one(self):
        self.assertEquals(named_tuple(),78.00)
        '''5
ID         MARKS      NAME       CLASS
1          97         Raymond    7
2          50         Steven     4
3          91         Adrian     9
4          72         Stewart    5
5          80         Peter      6'''
    def test_two(self):
        self.assertEquals(named_tuple(), 81.00)

    '''5
MARKS      CLASS      NAME       ID
92         2          Calum      1
82         5          Scott      2
94         2          Jason      3
55         8          Glenn      4
82         2          Fergus     5'''

    def test_three(self):
        self.assertEquals(named_tuple(),80.80)
    '''5
CLASS      NAME       MARKS      ID
4          Iain       96         1
2          Jeremy     77         2
5          Derek      94         3
4          Ryan       52         4
3          Leslie     85         5'''