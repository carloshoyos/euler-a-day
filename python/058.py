"""
Project Euler Problem 58
========================

Starting with 1 and spiralling anticlockwise in the following way, a
square spiral with side length 7 is formed.

                           37 36 35 34 33 32 31
                           38 17 16 15 14 13 30
                           39 18  5  4  3 12 29
                           40 19  6  1  2 11 28
                           41 20  7  8  9 10 27
                           42 21 22 23 24 25 26
                           43 44 45 46 47 48 49

It is interesting to note that the odd squares lie along the bottom right
diagonal, but what is more interesting is that 8 out of the 13 numbers
lying along both diagonals are prime; that is, a ratio of 8/13 62%.

If one complete new layer is wrapped around the spiral above, a square
spiral with side length 9 will be formed. If this process is continued,
what is the side length of the square spiral for which the ratio of primes
along both diagonals first falls below 10%?
"""

# approach 1 - reuse problem 28 (spires) and 41 (prime testing)
# You can tell bottom right diagonal value is (2n-1)^2, and subtract (2n-1), 2*(2n-1) and 3*(2n-1) to get the other 3 diagonals
# approach 2 - to speed things up as prime testing get real large, use Miller-Rabin algorithm


import math, itertools
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



diagonals = [1]
prime_count = 0
for n in itertools.count(2,1):
    newline = [(2*n - 1) ** 2 - 2*i*(n-1) for i in [3,2,1,0]]
    prime_count += len([x for x in newline if isPrime(x)])
    diagonals += newline

    if(prime_count / len(diagonals) < 0.1):
        #print(n, 2*n-1, prime_count, len(diagonals), prime_count / len(diagonals))#, diagonals)
        print(2*n-1)
        break