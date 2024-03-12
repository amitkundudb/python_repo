#This is a program to find the second most number in a list
#Here I have also included some edge cases
#In case of error it will give error message "-1"

import logging

def find_second_most_number():
    logging.basicConfig(level=logging.INFO,format='%(message)s')
    n = int(input().strip())
    arr = list(map(int, input().strip().split()))
    arr_set = set(arr)
    unique_arr = sorted(arr_set, reverse=True)
    if len(unique_arr) > 1:
        logging.info(unique_arr[1])
    else:
        logging.error("-1")