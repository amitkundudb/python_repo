'''Task:
You are given a 2-D array of size N*M.
Your task is to find:---------
The mean along axis 1
The var along axis 0
The std along axis NONE '''
import numpy as np
import logging
logging.basicConfig(level=logging.INFO,format='%(message)s')

def mean_var_std_fn():
    N, i = map(int, input().split())
    arr = np.array([list(map(int, input().split())) for i in range(N)])
    result = '\n'.join([
        f"{np.mean(arr, axis=1)}",
        f"{np.var(arr, axis=0)}",
        f"{round(np.std(arr), 11)}"
    ])
    logging.info(result)