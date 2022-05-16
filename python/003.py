"""
Project Euler Problem 3
=======================

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143?
"""


from math import gcd

# Bread and butter problem.  Two approaches.  The  direct "brute force", and an advanced pollard function.   For the small integer in this problem both functions have the same performance. Pollard performs better for larger integers with one small factor.  


## performance
#  for approach (a) (iteration), there are two functions. a1 (easySum) is the typical c style of loop and if, while a2 (pythonicSum) is all in one line 
#  performance calculated using `python -m cProfile 001.py` 

## n -                                      factorization     pollard
## 600851475143                             0.002             0.002
## 600851475143600851475143600851475143     120.002           1.362

# a) the easy way is to divide by all factors until the number.   
# Two easy ways to improve it: i) divide only by odd numbers after rulling out powers of 2, and ii) divide only until floor(sqr(n))

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

# b) being more efficient using Pollard's algorithm  https://en.wikipedia.org/wiki/Pollard%27s_rho_algorithm (complexity depends on smallest factor)
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


if __name__ == "__main__":
    #print( factorization(600851475143600851475143600851475143) )
    #print( pollard_factorization(600851475143600851475143600851475143) )
    print( max(pollard_factorization(600851475143)) )