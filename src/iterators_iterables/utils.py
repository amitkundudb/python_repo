'''You are given a list of  lowercase English letters.
 For a given integer ,
 select any  indices (assume -based indexing)
  with a uniform probability from the list.'''

from itertools import combinations
import logging

logging.basicConfig(level=logging.INFO, format='%(message)s')


def iterables_iterators():
    N = int(input())
    l = input().split()
    K = int(input())
    newl = list(combinations(l, K))
    length = 0
    for i in newl:
        if 'a' in i:
            length += 1
    ratio = length / len(newl)
    logging.info(round(ratio, 3))
    return round(ratio, 3)
