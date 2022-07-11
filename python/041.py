"""
Project Euler Problem 41
========================

We shall say that an n-digit number is pandigital if it makes use of all
the digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital
and is also prime.

What is the largest n-digit pandigital prime that exists?
"""


# method 1:  reusing problems 7 (sieve to calculate primes up to n) and filter using problem 38 (pandigital evaluation) to find all pandigital primes. 
# note that performance is very bad..  this onyl works if we reduce the solution space.. note that no solution exists for 8 or 9 digits because 1+ 2 + 3 + 4 + 5 + 6 + 7 + 8 = 36 is divisble by 3 and thus not prime (same with numbers until 9).

# method 2: generating all good pandigital numbers and evaluate for primality


import math 
import itertools



# returns a set with all primes under n
def sieve_for_primes_to(n):
    size = n//2
    prime_list = [x if (x%2 != 0) or (x == 2) else 0 for x in range(0,n+1)]

    sqrt_n = int(n**0.5)  # only sieve until square root of max value 
    for i in range(3,sqrt_n+1):
        if prime_list[i]:  # remove all factors of a prime number
            prime_list[i*2::i] = [0] * (n // i - 1)  # mark as zero for deletion 

    
    # remove non primes 
    prime_list = [x for x in prime_list if x > 1]
    return set(prime_list)

# checks if number n is pandigital
def isPandigital(x):
    x = str(x)
    return "".join(sorted(x)) == "123456789"[0:len(x)]


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



def calculatepandigitalPrime_sieve():
    primes = sieve_for_primes_to(10**7)  #  

    return max( [x for x in primes if isPandigital(x)]) 


# 
def calculatepandigitalPrime_perm():

    for i in reversed(range(2,9)):   # digits from 2 to 9 lenghts
        for n in itertools.permutations("123456789"[0:i], i): 
            testnum = int("".join(n))
            if int(n[-1]) %2 != 0 and isPrime(testnum): 
                return testnum 

    return None
# method 1 
#print(calculatepandigitalPrime_sieve()) # this takes forever, can cheat by reducing the solution space 

#method 2 - calculate all permutations
print(calculatepandigitalPrime_perm())
