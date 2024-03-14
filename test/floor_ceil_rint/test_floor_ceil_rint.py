import unittest
from src.floor_ceil_rint.utils import floorceilrent


class FloorCeilRintTest(unittest.TestCase):
    def test_one(self):
        self.assertEquals(floorceilrent(),    '''[ 1.  2.  3.  4.  5.  6.  7.  8.  9.]
[  2.   3.   4.   5.   6.   7.   8.   9.  10.]
[  1.   2.   3.   4.   6.   7.   8.   9.  10.]''')
    '''1.1 2.2 3.3 4.4 5.5 6.6 7.7 8.8 9.9'''


    def test_two(self):
        self.assertEquals(floorceilrent(), '''[ 2.  3.  4.  5.  6.  7.  8.]
[ 3.  4.  5.  6.  7.  8.  9.]
[ 2.  3.  4.  6.  7.  8.  9.]''')

    '''2.2 3.3 4.4 5.5 6.6 7.7 8.8
'''

    def test_three(self):
        self.assertEquals(floorceilrent(), '''[ 1.  2.  3.  4.  5.  6.  7.  8.]
[ 2.  3.  4.  5.  6.  7.  8.  9.]
[ 1.  2.  3.  4.  6.  7.  8.  9.]''')
    '''1.1 2.2 3.3 4.4 5.5 6.6 7.7 8.8'''