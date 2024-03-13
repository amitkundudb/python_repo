import datetime
import logging

logging.basicConfig(level=logging.INFO, format='%(message)s')


def time_delta():
    num_test_cases = int(input())
    for _ in range(num_test_cases):
        t1_str = input()
        t2_str = input()
        t1 = datetime.datetime.strptime(t1_str, "%a %d %b %Y %H:%M:%S %z")
        t2 = datetime.datetime.strptime(t2_str, "%a %d %b %Y %H:%M:%S %z")
        delta = abs(t1 - t2).total_seconds()
        result = int(delta)  # Convert to integer for the final result
        logging.info(result)
