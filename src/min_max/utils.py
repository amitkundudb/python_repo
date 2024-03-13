#Given a 2-D array with dimensions N*M
#Task is to perform the min function over axis  and then find the max of that
"""I have used numpy library to solve this problem"""
import numpy as np
import logging

logging.basicConfig(level=logging.INFO,format='%(message)s')
def minmax():
    N, i = input().split()
    N = int(N)

    arr = [list(map(int, input().split())) for i in range(N)]
    logging.info(np.max(np.min(np.array(arr), axis=1)))