#!/bin/python3

#
# Complete the 'readKeystrokes' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. STRING keystrokes
#

def readKeystrokes(n, keystrokes):
    stack = []
    for char in keystrokes:
        if char != '<':
            stack.append(char)
        elif stack:
            stack.pop()
    print("".join(stack))

if __name__ == '__main__':
    n = int(input().strip())

    keystrokes = input()

    readKeystrokes(n, keystrokes)