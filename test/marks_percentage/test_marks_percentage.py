import unittest
from src.marks_percentage.utils import average_marks


class MarksPercentageTest(unittest.TestCase):
    def test_one(self):
        self.assertEquals(average_marks(),    26.5)
    '''2
Harsh 25 26.5 28
Anurag 26 28 30
Harsh'''


    def test_two(self):
        self.assertEquals(average_marks(), 56.00)

    '''3
Krishna 67 68 69
Arjun 70 98 63
Malika 52 56 60
Malika
'''

    def test_three(self):
        self.assertEquals(average_marks(),60.00 )
    '''3
Riya 52 93 20
Rencho 69 65 62
Hbtg 52 60 68
Hbtg'''