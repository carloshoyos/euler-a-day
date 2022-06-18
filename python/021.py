"""
Project Euler Problem 21
========================

Let d(n) be defined as the sum of proper divisors of n (numbers less than
n which divide evenly into n).
If d(a) = b and d(b) = a, where a =/= b, then a and b are an amicable pair
and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22,
44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1,
2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
"""
from math import isqrt

# two approaches.
# 1- brute force, for each number calculate all of its divisors.  Oddly 
# 2- a sieve like approach...  generate a matrix of 10000 numbers, and for each x in the matrix, add x as a divisor of 2x, 3x, 4x ...  

## performance
#  the brute force approach is not 
## n -      divisors      sieve    
## 10000     5.283        4.224          
   



# plan 1, brute force approach
def getAllDivisorsBrute(ceiling): 
	# Returns a list of all divisors for numbers up to ceiling 
    # for example, position 220 has [1, 2, 4, 5, 10, 11, 20, 22, 44, 55, 110]
    divisors = [[1] for i in range(0, ceiling+1)] 
    for x in range(2, ceiling+1):
        for j in range(2, x//2+1):
            if x%j == 0:
                divisors[x].append(j)
    return divisors

# plan 2, fast and sweet 
def getAllDivisors(ceiling): 
	# Returns a list of all divisors for numbers up to ceiling 
    # for example, position 220 has [1, 2, 4, 5, 10, 11, 20, 22, 44, 55, 110]
    divisors = [[1] for i in range(0, ceiling+1)] 
    for x in range(2, ceiling+1):
        for j in range(x * 2, ceiling+1, x):
            divisors[j].append(x)
    return divisors

import sys

if __name__ == "__main__":
    # usage..  021.py high_limit method{'sieve' | 'divisors' }

    try:
        ceiling = int(sys.argv[1])
        method_to_use = sys.argv[2]
    except IndexError:
        ceiling = 10000      # run with default 10000
        method_to_use = 'sieve'  # and use default easy method if none provided

    amicable_sum = 0 
    if method_to_use == 'divisors':
        divisors = getAllDivisorsBrute(ceiling)
        divisorsums = [sum(x) for x in divisors]


        for i in range(1, ceiling+1):
            for j in range (i+1, ceiling +1):
                if divisorsums[j]== i and divisorsums[i] == j:
                    amicable_sum = amicable_sum + i + j

        print(amicable_sum)
    if method_to_use == 'sieve':
        divisors = getAllDivisors(ceiling)
        divisorsums = [sum(x) for x in divisors]


        for i in range(1, ceiling+1):
            for j in range (i+1, ceiling +1):
                if divisorsums[j]== i and divisorsums[i] == j:
                    amicable_sum = amicable_sum + i + j

        print(amicable_sum)


