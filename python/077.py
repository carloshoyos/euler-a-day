"""
Project Euler Problem 77
========================

It is possible to write ten as the sum of primes in exactly five different
ways:

7 + 3
5 + 5
5 + 3 + 2
3 + 3 + 2 + 2
2 + 2 + 2 + 2 + 2

What is the first value which can be written as the sum of primes in over
five thousand different ways?
"""

# This was a nice problem to play with on paper.  
# approach 1: Based on what I learned from problem 77, I started generating all sums with one prime at a time, and then adding more primes. 
# for the first prime p1, the only digits that have a solution are p1, 2*p1 (p1+p1), 3*p1 (p1+p1+p1) etc.. 
# then adding the next prime p2, you add to each of the solutions above, as well as the new solutions (which covers for 2*p2, 3*p2, etc..)

# approach 2: recursively generate all the sums:
# for a number n, define f(n, k) as the sums totaling n using primes p1 to pk
# then f(n, k) = f(n, k-1) + f(n-pk, k)  ## first part is the sums using all but the last prime, + all sums totaling n-k

import math
import functools


upper_limit = 80  # this is a little hacky in that I set an upper limit to generate the partitions and then find the minimum number that has over 5000 

@functools.cache
def is_prime(x):
    if x <= 1:
        return False
    elif x <= 3:
        return True
    elif x % 2 == 0:
        return False
    else:
        for i in range(3, math.isqrt(x) + 1, 2):
            if x % i == 0:
                return False
        return True

def countPrimeSubPartitions(upper_limit):

    ways = [0] * (upper_limit+1)

    for prime in range(1, upper_limit+1):
        if not is_prime(prime): continue


        # you can write prime as the sum of prime (prime = prime)
        ways[prime] += 1    

        # and for every other number n, if there were k sums s_1, ... s_k, then n+prime will have k new sums s_1+prime, .... s_k+prime 
        # so n+prime  will have k new ways (where k were all the ways to sum n with primes < prime) 
        for j in range(0, upper_limit-prime+1):
            ways[j+prime] += ways[j]

    return(ways)


# approach 1 - generating all sums with one prime at a time,
parts = countPrimeSubPartitions(upper_limit)

for i, j in enumerate(parts):
    if j>5000: 
        print(i)
        break


# approach 2 - recursive
# for a number n, define f(n, k) as the sums totaling n using primes p1 to pk
# then f(n, k) = f(n, k-1) + f(n-pk, k)  ## first part is the sums using all but the last prime, + all sums totaling n-k


prime_numbers = [x for x in range (upper_limit+1) if is_prime(x) if is_prime(x) ]

def countPrimeSubPartForkPrimes(number, k):
    global prime_numbers
    if number < 0 or k < 0: return 0
    if number == 0: return 1 
    else:
        return countPrimeSubPartForkPrimes(number, k-1) + countPrimeSubPartForkPrimes(number-prime_numbers[k], k)


for n in range(10, upper_limit):
    if countPrimeSubPartForkPrimes(n,len(prime_numbers)-1) > 5000:
        print(n)
        break

