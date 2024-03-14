"""Find the determinant of a square matrix using numpy
numpy.linalg.det([[1 , 2], [2, 1]])
linalg.det is used to find determinant"""


import numpy
import logging
logging.basicConfig(level=logging.INFO,format='%(message)s')

def linearalgebra():
    mtx_size = int(input())
    mtx_a = []
    for _ in range(mtx_size):
        row = list(map(float, input().split()))
        mtx_a.append(row)
    mtx_det = round(numpy.linalg.det(mtx_a), 2)
    logging.info(mtx_det)
    return mtx_det