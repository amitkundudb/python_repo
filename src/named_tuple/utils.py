#calculates the average marks of students using a namedtuple
import logging
from collections import namedtuple

logging.basicConfig(level=logging.INFO,format='%(message)s')
def named_tuple():
    N = int(input())
    Sheet = namedtuple('Sheet', input().split())
    marks= [Sheet._make(input().split()).MARKS for i in range(N)]
    logging.info(sum(map(int, marks))/N)
    return sum(map(int, marks))/N