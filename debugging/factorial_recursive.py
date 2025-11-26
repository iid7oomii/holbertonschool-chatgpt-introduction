#!/usr/bin/python3
import sys

def factorial(n):
    """
    Function description: Recursive function to find the factorial of an integer
    Parameters: n: integer number
    Returns: the factorial of n
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

f = factorial(int(sys.argv[1]))
print(f)
