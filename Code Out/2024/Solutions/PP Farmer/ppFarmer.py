#!/bin/python3

from math import ceil

#
# Complete the 'minimumPerfPoints' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER m
#  3. INTEGER_ARRAY p
#

def minimumPerfPoints(n, m, p):
    p.sort(reverse=True)
    weighted = [v * 0.95 ** i for i, v in enumerate(p)]

    total = sum(weighted)

    if total >= m:
        print(-1)
        return

    diff = m - total * 0.95
    min_pp = 1e17
    for i in range(n+1):
        pp = diff / 0.95**i
        min_pp = min(min_pp, pp)
        if i < n:
            diff += weighted[i]*0.95 - weighted[i]
    print(ceil(min_pp))

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    p = list(map(int, input().rstrip().split()))

    minimumPerfPoints(n, m, p)