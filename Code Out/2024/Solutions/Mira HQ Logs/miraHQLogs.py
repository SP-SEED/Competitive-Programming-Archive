#!/bin/python3

#
# Complete the 'countImposters' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY p
#  3. INTEGER_ARRAY q
#

def countImposters(n, p, q):
    prev = [0] * 10_001
    imposters = [0] * 10_001
    for i in range(n):
        if imposters[p[i]]: continue
        if prev[p[i]] == None: prev[p[i]] = q[i]
        elif prev[p[i]] == q[i]: prev[p[i]] = None
        else: imposters[p[i]] = 1
    if any(imposters):
        print(*[i for i, imposter in enumerate(imposters) if imposter])
    else:
        print(-1)

if __name__ == '__main__':
    n = int(input().strip())

    p = list(map(int, input().rstrip().split()))

    q = list(map(int, input().rstrip().split()))

    countImposters(n, p, q)