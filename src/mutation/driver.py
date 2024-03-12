from src.mutation.utils import *

import logging
logging.basicConfig(level=logging.INFO,format='%(message)s')
if __name__ == '__main__':
    string = input()
    position = int(input())
    character = input()
    mutated_string = mutate_string_and_return(string, position, character)
    logging.info(mutated_string)
