#!/bin/python3

import collections

#
# Complete the 'countValid' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. STRING_ARRAY codes
#

def countValid(n, codes):
    count = 0
    for s in codes:
        val, code = s.split(".")
        if not val:
            count += 1
            continue
        elif len(val) == len(code):
            count += val == code
            continue
        queue = collections.deque(list(val))
        for char in code:
            if char == queue[0]:
                queue.popleft()
            if not len(queue):
                count += 1
                break
    print(count)

if __name__ == '__main__':
    n = int(input().strip())

    codes = []

    for _ in range(n):
        codes_item = input()
        codes.append(codes_item)

    countValid(n, codes)