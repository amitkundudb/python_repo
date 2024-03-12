import logging

def mutate_string_and_return(string, position, character):
    logging.basicConfig(level=logging.INFO,format='%(message)s')
    l = list(string)
    l[position] = character
    string = ''.join(l)
    return string