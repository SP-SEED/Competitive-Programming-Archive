#!/bin/python3

import bisect
from math import gcd

#
# Complete the 'countFractions' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER x
#  3. INTEGER y
#  4. INTEGER z
#  5. INTEGER w
#  6. FLOAT_ARRAY k
#

def countFractions(n, x, y, z, w, k):
    values = [i/j for i in range(x, y+1) for j in range(z, w+1) if gcd(i, j) == 1]
    values.sort()
    count = [bisect.bisect(values, ki) for ki in k]
    print(*count)

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    x = int(first_multiple_input[1])

    y = int(first_multiple_input[2])

    z = int(first_multiple_input[3])

    w = int(first_multiple_input[4])

    k = list(map(float, input().rstrip().split()))

    countFractions(n, x, y, z, w, k)