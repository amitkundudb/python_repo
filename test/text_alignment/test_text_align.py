import unittest
from src.text_alignment.utils import text_alignment


class TextAlignTest(unittest.TestCase):
    def test_one(self):
        self.maxDiff = None
        self.assertEqual(text_alignment(), '''    H    
   HHH   
  HHHHH  
 HHHHHHH 
HHHHHHHHH
  HHHHH               HHHHH             
  HHHHH               HHHHH             
  HHHHH               HHHHH             
  HHHHH               HHHHH             
  HHHHH               HHHHH             
  HHHHH               HHHHH             
  HHHHHHHHHHHHHHHHHHHHHHHHH   
  HHHHHHHHHHHHHHHHHHHHHHHHH   
  HHHHHHHHHHHHHHHHHHHHHHHHH   
  HHHHH               HHHHH             
  HHHHH               HHHHH             
  HHHHH               HHHHH             
  HHHHH               HHHHH             
  HHHHH               HHHHH             
  HHHHH               HHHHH             
                    HHHHHHHHH 
                     HHHHHHH  
                      HHHHH   
                       HHH    
                        H     ''')
        '''5'''
    def test_two(self):
        self.maxDiff = None
        self.assertEqual(text_alignment(), '''  H  
 HHH 
HHHHH
 HHH         HHH        
 HHH         HHH        
 HHH         HHH        
 HHH         HHH        
 HHHHHHHHHHHHHHH  
 HHHHHHHHHHHHHHH  
 HHH         HHH        
 HHH         HHH        
 HHH         HHH        
 HHH         HHH        
            HHHHH 
             HHH  
              H   ''')
    '''3'''

    def test_three(self):
        self.maxDiff = None
        self.assertEqual(text_alignment(),'''     H     
    HHH    
   HHHHH   
  HHHHHHH  
 HHHHHHHHH 
HHHHHHHHHHH
   HHHHHH                  HHHHHH               
   HHHHHH                  HHHHHH               
   HHHHHH                  HHHHHH               
   HHHHHH                  HHHHHH               
   HHHHHH                  HHHHHH               
   HHHHHH                  HHHHHH               
   HHHHHH                  HHHHHH               
   HHHHHHHHHHHHHHHHHHHHHHHHHHHHHH   
   HHHHHHHHHHHHHHHHHHHHHHHHHHHHHH   
   HHHHHHHHHHHHHHHHHHHHHHHHHHHHHH   
   HHHHHH                  HHHHHH               
   HHHHHH                  HHHHHH               
   HHHHHH                  HHHHHH               
   HHHHHH                  HHHHHH               
   HHHHHH                  HHHHHH               
   HHHHHH                  HHHHHH               
   HHHHHH                  HHHHHH               
                        HHHHHHHHHHH 
                         HHHHHHHHH  
                          HHHHHHH   
                           HHHHH    
                            HHH     
                             H      ''')
    '''6'''