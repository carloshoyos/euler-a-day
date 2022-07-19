"""
Project Euler Problem 47
========================

The first two consecutive numbers to have two distinct prime factors are:

14 = 2 * 7
15 = 3 * 5

The first three consecutive numbers to have three distinct prime factors
are:

644 = 2^2 * 7 * 23
645 = 3 * 5 * 43
646 = 2 * 17 * 19.

Find the first four consecutive integers to have four distinct primes
factors. What is the first of these numbers?
"""

# reusing factorization function from problem 3.
# Note that brute force factorization is too slow, have to use pollard faactorization to be effective 

from math import gcd

def factorization(n):
    factors = []
    factor = 2
    while n>1: 
        if (n % factor) == 0 : 
            factors.append(factor)
            n = n / factor
        else:
            factor = factor + 1
    return factors

def pollard_factorization(n):

    factors = []

    def get_factor(n):
        x_fixed = 2
        cycle_size = 2
        x = 2
        factor = 1

        while factor == 1:
            for count in range(cycle_size):
                if factor > 1: break
                x = (x * x + 1) % n
                factor = gcd(x - x_fixed, n)

            cycle_size *= 2
            x_fixed = x

        return factor

    while n > 1:
        next = get_factor(n)
        factors.append(next)
        n //= next

    return factors


factor_count = 4
n = 9
while True: 
    if all(len(set(pollard_factorization(n+i))) == factor_count for i in range(0,factor_count)):
        break
    n += 1

print(n)


