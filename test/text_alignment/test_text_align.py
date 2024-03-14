import unittest
from src.text_alignment.utils import text_alignment


class TextAlignTest(unittest.TestCase):
    def test_one(self):
        self.assertEquals(text_alignment(),'''''')
        '''3'''
    def test_two(self):
        self.assertEquals(text_alignment(), '''''')
    ''''''

    def test_three(self):
        self.assertEquals(text_alignment(),'''''')
    ''''''