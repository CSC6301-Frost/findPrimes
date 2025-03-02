""" CSC 6301 - Assignment 7
Jeffrey Frost
Version 1.0
"""


import random

def guess():
    """guess function generates a random integer starting from 2 to 5000

    Returns:
        int: random integer from 2 to 5000
    """
    return random.randint(2, 5000)

def isPrime(x):
    """isPrime function determine whether the argument x is a prime number or not.  x must be an integer
    to avoid a typeError at the range function.

    Args:
        x (int): candidate value to determine whether it is a prime number or not

    Returns:
        boolean: True if prime number / False if not prime number
    """
    for i in range(x):
        for j in range(x):
            if i * j == x:
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

