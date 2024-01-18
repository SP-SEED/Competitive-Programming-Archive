#!/bin/python3

#
# Complete the 'tally' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER m
#  3. INTEGER_ARRAY t
#  4. INTEGER_ARRAY k
#

def tally(n, m, t, k):
    if not (n and (not(n & (n - 1)))): # n is not power of 2
            for j in range(5):
                n |= n >> (2**j)
            n += 1 # change n to be the next closest power of 2

    tally = [0, 0, 0] # fire, grass, water

    # build segment trees
    N = 2**21
    tree = [''] * (2 * N)

    # insert nodes
    for j in range(len(t)):
        tree[n+j] = str(t[j])
    # calculate parent nodes
    for j in range(n - 1, 0, -1):
        a, b = tree[j << 1], tree[j << 1 | 1]
        # determine the winner
        if not b or a == b or a == "0" and b == "1" or a == "1" and b == "2" or a == "2" and b == "0":
            tree[j] = a
        else:
            tree[j] = b

    # loop through all queries
    for num in k:
        winner = '' # store winner of considered subsection
        a, b = n, num+n
        while a < b:
            if a & 1:
                elem = tree[a]
                if not winner or elem == winner or elem == "0" and winner == "1" or elem == "1" and winner == "2" or elem == "2" and winner == "0":
                    winner = elem
                a += 1

            if b & 1:
                b -= 1
                elem = tree[b]
                if not winner or elem == winner or elem == "0" and winner == "1" or elem == "1" and winner == "2" or elem == "2" and winner == "0":
                    winner = elem

            a >>= 1
            b >>= 1

        tally[int(winner)] += 1

    print(*tally)

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    t = list(map(int, input().rstrip().split()))

    k = list(map(int, input().rstrip().split()))

    tally(n, m, t, k)