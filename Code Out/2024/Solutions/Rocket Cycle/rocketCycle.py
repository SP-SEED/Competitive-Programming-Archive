#!/bin/python3

import math

#
# Complete the 'countHits' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER r
#  3. INTEGER a
#  4. INTEGER b
#  5. INTEGER_ARRAY x
#  6. INTEGER_ARRAY y
#

def countHits(n, r, a, b, x, y):
    count = 0
    for px, py in zip(x, y):
        if math.sqrt((px-a)**2 + (py-b)**2) <= r:
            count += 1
    print(count)

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    r = int(first_multiple_input[1])

    second_multiple_input = input().rstrip().split()

    a = int(second_multiple_input[0])