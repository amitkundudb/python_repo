# This function takes a string, a position, and a character as input
# Replaces the character at the specified position in the string,
# then returns the mutated string
import logging


def mutate_string_and_return(string, position, character):
    logging.basicConfig(level=logging.INFO, format='%(message)s')
    l = list(string)
    l[position] = character
    string = ''.join(l)
    return string


string = input()
position = int(input())
character = input()
