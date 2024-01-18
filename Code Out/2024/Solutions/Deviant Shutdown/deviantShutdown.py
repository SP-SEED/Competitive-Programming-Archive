#!/bin/python3

#
# Complete the 'countCombinations' function below.
#
# The function accepts INTEGER n as parameter.
#

def countCombinations(n):
    # if value too small then write 0
    if n < 6:
        print(0)
        return

    # generate list of primes using sieve of eratosthenes
    primes = [2]
    for j in range(3, n-4, 2):
        isprime = True
        for prime in primes:
            if not (j % prime):
                isprime = False
                break
        if isprime: primes.append(j)

    count = 0

    # iterate over list
    for j, a in enumerate(primes):
        # two pointers to find pair
        l, r = j+1, len(primes)-1
        while l < r:
            s = primes[l] + primes[r] + a
            if s < n:
                l += 1
            elif s > n:
                r -= 1
            else:
                count += 1
                break

    print(count)

if __name__ == '__main__':
    n = int(input().strip())

    countCombinations(n)