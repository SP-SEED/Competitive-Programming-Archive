#!/bin/python3

#
# Complete the 'countValid' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY running_counts
#

def countValid(n, running_counts):
    count = 0
    for tc in running_counts:
        tally = [20, 12, 20] # 2-6, 7-9, 10-A
        for j, e in enumerate(tc):
            d = e if j == 0 else e - tc[j-1]
            d += 1
            tally[d] -= 1
        if not any(tally):
            count += 1
    print(count)

if __name__ == '__main__':
    n = int(input().strip())

    running_counts = []

    for _ in range(n):
        running_counts.append(list(map(int, input().rstrip().split())))

    countValid(n, running_counts)