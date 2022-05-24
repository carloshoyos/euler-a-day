"""
Project Euler Problem 5
=======================

2520 is the smallest number that can be divided by each of the numbers
from 1 to 10 without any remainder.

What is the smallest number that is evenly divisible by all of the numbers
from 1 to 20?
"""
#  First implementation is  straight forward using the definition of lcm: 
#  lcm(x,y) = x * y // gcd(x, y), and 
#  lcm(x,y,z) = lcm(x, lcm(y,z)) 

#  Second one is a more too complex approach: factorize each number in the range and for each prime factor find its maximum exponent. 
# The product of those primes ^ max exponent will be the lcm. 

## performance
#  gcd (euclid's algorithm) should be O(n) https://en.wikipedia.org/wiki/Euclidean_algorithm#Algorithmic_efficiency although for larger digits the % operation will have a bigger impact. 
#  the factorize method is not very efficient in this implementation as we iterate through all numbers. cd pcd
## n -      GCD      factorize    
## 10000     0.038   3.902          
## 20000     0.124   13.954      

        
import sys
import math

def gcd(x, y):
    while y:      
        x, y = y, x % y   # in python the evaluation order of multiple assignment is that all left side expressions ar e
    return x


# calculate the lcm for a group of integers 1 to n
def lcm_1ton_gcd(n):
    answer = 1
    for i in range(1, n+1):
        answer *= i // gcd(i, answer)
    return answer


# for approach #2 - a method to factorize a number 

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

from collections import Counter

def lcm_1ton_maxexp(max_value):
    lcm = [2]
    for i in range(3,max_value+1):
        factors = factorization(i)
        c = Counter(factors)
        c.subtract(Counter(lcm))
        lcm += list(c.elements())
    return(math.prod(lcm))


if __name__ == "__main__":
    # usage..  005.py max_range method{'gcd' | 'maxexp' }
    try:
        input_value = int(sys.argv[1])
        method_to_use = sys.argv[2]
    except IndexError:
        input_value = 20      # run with default input 1000 
        method_to_use = 'gcd'  # and use default easy method if none provided


    if method_to_use == 'gcd':
        print(lcm_1ton_gcd(input_value))

    if method_to_use == 'maxexp':
        print(lcm_1ton_maxexp(input_value))    

    # for i in range(100000,100001):
    #     print(i, lcm_1ton_gcd(i), "\n")
    #     print(i, lcm_1ton_maxexp(i))
