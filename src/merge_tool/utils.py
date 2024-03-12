import logging
logging.basicConfig(level=logging.INFO,format='%(message)s')
def merge_the_tools(s, k):
    substrings = [s[i:i+k] for i in range(0, len(s), k)]
    for substring in substrings:
        seen = set()
        result = ""
        for char in substring:
            if char not in seen:
                result += char
                seen.add(char)
        logging.info(result)

s = input()
k = int(input())
