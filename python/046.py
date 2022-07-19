"""
Project Euler Problem 46
========================

It was proposed by Christian Goldbach that every odd composite number can
be written as the sum of a prime and twice a square.

9 = 7 + 2 * 1^2
15 = 7 + 2 * 2^2
21 = 3 + 2 * 3^2
25 = 7 + 2 * 3^2
27 = 19 + 2 * 2^2
33 = 31 + 2 * 1^2

It turns out that the conjecture was false.

What is the smallest odd composite that cannot be written as the sum of a
prime and twice a square?
"""

# brute force..  reusing problem 41 functions for isprime testing.  The counter example is small enough that we don't need a sieve   
import math
import itertools


# check if number is prime (via division)
def isPrime(x):

    # get trivial cases out of the way 
    if x == 2 or x == 3:
        return True
    elif x % 2 == 0 or x <= 1:
        return False
    else:
        for i in range(3, math.isqrt(x) + 1, 2):
            if x % i == 0:
                return False
        return True


# checks is number can be written as the sum of a prime and twice a square.
def isCompositePrimeAndSquareSum(n):

    if n % 2 == 0 or isPrime(n): return False
    for i in range(1, math.isqrt(n)+1):
        if n - 2* i ** 2 < 0:
            return False
        elif isPrime(n - 2* i ** 2):
            return True

# approach 1, iterate through all odd numbers and discard primes or those that match the rule
# we can start after 9
i = 9
while True:
    i += 2
    if isPrime(i): continue  # only check odd composite numbers
    if not isCompositePrimeAndSquareSum(i): 
        print(i) 
        break

# Same, but written in a more pythonic way using itertools 
it = itertools.filterfalse(lambda x: isCompositePrimeAndSquareSum(x) or isPrime(x), itertools.count(9,2))
print(next(it))
