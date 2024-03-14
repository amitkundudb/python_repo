'''The first line contains the number of test cases.
For each test case, there are 2 lines.
The first line of each test case contains , the number of cubes.
The second line contains  space separated integers, denoting the sideLengths of each cube.'''
import logging
logging.basicConfig(level=logging.INFO,format='%(message)s')
def piling_up():
    t = int(input())
    for i in range(t):
        n = int(input())
        l = list(map(int, input().split()))
        b = []
        while len(l) > 0:
            if l[-1] > l[0]:
                b.append(l.pop(-1))
            else:
                b.append(l.pop(0))
        c = b.copy()
        b.sort(reverse=True)
        if b == c:
            logging.info('Yes')
            return 'Yes'
        else:
            logging.info('No')
            return 'No'