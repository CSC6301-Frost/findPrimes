""" CSC 6301 - Assignment 7
Jeffrey Frost
Version 1.1
"""


import random

def guess():
    """guess function generates a random integer starting from 2 to 5000

    Returns:
        int: random integer from 2 to 5000
    """
    return random.randint(2, 5000)

def isPrime(x):
    """isPrime function determine whether the argument x is a prime number or not.  This implementation is from CSC-6303 week 2 C++ code example

    Args:
        x (int): candidate value to determine whether it is a prime number or not

    Returns:
        boolean: True if prime number / False if not prime number
    """
    if (x <= 1):
        return False
    elif (x <= 3):
        return True
    elif (x % 2 == 0 ) or (x % 3 == 0):
        return False
    else:
        for i in range(5, x, 6):
            if (x % i == 0) or (x % (i + 2) == 0):
                return False
    return True

def findPrimes(num):
    """findPrimes function chooses a random number, which it then determines is a prime number or not.  
    This effort is repeated for as many times as the argument num specifies.

    Args:
        num (int): specifies the amount of random numbers to generate

    Returns:
        int[]: list of the prime numbers found
    """
    primes = []
    for i in range(num):
        p = guess()
        while not isPrime(p):
            p = guess()
        primes += [p]
    return primes

import cProfile
cProfile.run('print(findPrimes(500)[:10])')

