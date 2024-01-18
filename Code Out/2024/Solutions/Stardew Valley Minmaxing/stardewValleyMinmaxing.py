#!/bin/python3

#
# Complete the 'maximumGold' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER m
#  3. INTEGER p
#  4. INTEGER_ARRAY q
#  5. INTEGER_ARRAY r
#  6. INTEGER_ARRAY s
#

def maximumGold(n, m, p, q, r, s):
    table = [m] * n

    for j in range(1, n):
        for option in range(p):
            if not (j >= r[option] and table[j-r[option]] >= q[option]):
                continue
            units = table[j-r[option]] // q[option]
            revenue = table[j-r[option]] - q[option]*units + s[option]*units
            table[j] = max(revenue, table[j])

    print(table[-1])

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    p = int(first_multiple_input[2])

    q = list(map(int, input().rstrip().split()))

    r = list(map(int, input().rstrip().split()))

    s = list(map(int, input().rstrip().split()))

    maximumGold(n, m, p, q, r, s)