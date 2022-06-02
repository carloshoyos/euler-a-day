"""
Project Euler Problem 7
=======================

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see
that the 6th prime is 13.

What is the 10001st prime number?
"""

# yay - time to implement eratosthenes sieve.  Two methods:
# First brute force implementation, removes all multiples of each prime. 
# there are further ways to optimize, we don't need to keep all numbers (e.g. evens) in the sieve I just include them so that the index would match the number

# Second with a generator that yields the next prime number and keeps a 



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

# this was done in problem 10 
def generate_primes(upper_bound):
    # TODO, implement this
    # keep a list of primes, first time its called yield 2 and initialize the list with [2] and go to next odd number (3)
    # from there as long as that last odd number is less than upper bound
    # test division against list of primes 
    # if it divides, go to next odd number until one is not divisible by list of primes -> add to list and yield it
    # continue until hitting upper bound 
    return upper_bound


# generate all primes under 200000  (the nth prime should be around n log n but doubling hti)
print(sieve_for_primes_to(200000)[10000])

