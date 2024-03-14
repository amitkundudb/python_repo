#The code defines a function `merge_the_tools`
# that splits a string into substrings of a specified length,
# removes duplicate characters from each substring,
# and logs the resulting substrings.
import logging
logging.basicConfig(level=logging.INFO,format='%(message)s')
def merge_the_tools():
    s = input()
    k = int(input())
    results = []
    substrings = [s[i:i+k] for i in range(0, len(s), k)]
    for substring in substrings:
        seen = set()
        result = ""
        for char in substring:
            if char not in seen:
                result += char
                seen.add(char)
        logging.info(result)
        results.append(result)
    return '\n'.join(results)

