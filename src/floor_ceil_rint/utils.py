import numpy
import logging

logging.basicConfig(level=logging.INFO,format='%(message)s')
def floorceilrent():
    numpy.set_printoptions(legacy='1.13')
    A = numpy.array(list(map(float, input().split())))
    logging.info(f"{numpy.floor(A)}")
    logging.info(f"{numpy.ceil(A)}")
    logging.info(f"{numpy.rint(A)}")