'''Input Format
The first line contains the integer, .
The next  lines each contain a word.
Output Format--
On the first line, output the number of distinct words from the input.
On the second line, output the number of occurrences for each distinct word'''

from collections import Counter
import logging
logging.basicConfig(level=logging.INFO,format='%(message)s')
def word_order():
    n = int(input())
    words = [input().strip() for _ in range(n)]
    word_counts = Counter(words)
    logging.info(len(word_counts))
    logging.info(' '.join(map(str,word_counts.values())))