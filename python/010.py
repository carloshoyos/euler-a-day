"""
Project Euler Problem 10
========================

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""

# yay - get to test a prime number generator vs the sieve method from problem 7.   Spoiler, the sieve is way faster.
# For the generator just keep iterating through odd numbers and check divisibility against previous odd primes <= floor(sqrt(candidate))

## performance
#  Have to go to real large numbers to see a difference
## n -      generator      sieve    
## 2*10ˆ6     8.027        0.313          
## 2*10ˆ7     197.660      3.612 


from math import isqrt
import sys


def prime_generator(ceiling):
    i = 3
    primes = []  # will store all primes above 2 in this array to test future candidates 
    yield 2
    while i < ceiling:
        isprime = True
        for p in primes:    # check next odd number to see if its divisible by previous primes
            if i%p == 0:
                isprime = False
                break
            if p > isqrt(i):
                break
        
        if isprime:  # this is true if i was not divisible by all the odd primes < srt(i)
            primes.append(i)
            yield i 
        i += 2 

# explanation in problem 7
def sieve_for_primes_to(n):
    size = n//2
    prime_list = [x if (x%2 != 0) or (x == 2) else 0 for x in range(0,n+1)]

    sqrt_n = int(n**0.5)  # only sieve until square root of max value 
    for i in range(3,sqrt_n+1):
        if prime_list[i]:  # remove all factors of a prime number
            prime_list[i*2::i] = [0] * (n // i - 1)  # mark as zero for deletion 

    
    # remove non primes 
    prime_list = [x for x in prime_list if x > 1]
    return prime_list



if __name__ == "__main__":
    # usage..  006.py high_limit method{'formula' | 'iterate' }

    try:
        input_value = int(sys.argv[1])
        method_to_use = sys.argv[2]
    except IndexError:
        input_value = 2000000      # run with default input 2 million 
        method_to_use = 'sieve'  # and use default easy method if none provided

    sum = 0 
    if method_to_use == 'generator':
        for i in prime_generator(input_value):
            sum += i
        print(sum)

    if method_to_use == 'sieve':
        for i in sieve_for_primes_to(input_value):
            sum += i
        print(sum)



