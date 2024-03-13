import unittest
from src.calender_module.utils import get_day_of_week
class CalenderModuleTest(unittest.TestCase):
    def test_one(self):
        self.assertEquals(get_day_of_week(), "WEDNESDAY")
        '''03 14 2001'''

    def test_two(self):
        self.assertEquals(get_day_of_week(),"MONDAY")
    '''05 15 2000'''

    def test_three(self):
        self.assertEquals(get_day_of_week(), "THURSDAY")
        '''03 15 2001'''

