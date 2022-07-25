"""
Project Euler Problem 50
========================

The prime 41, can be written as the sum of six consecutive primes:

                       41 = 2 + 3 + 5 + 7 + 11 + 13

This is the longest sum of consecutive primes that adds to a prime below
one-hundred.

The longest sum of consecutive primes below one-thousand that adds to a
prime, contains 21 terms, and is equal to 953.

Which prime, below one-million, can be written as the sum of the most
consecutive primes?
"""


# using sieve (problem 7) to calculate list of all sorted primes below one million
# then iterate, for each prime find longest string of added primes. stop when sum is not a prime.

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



upper_limit = 10**6

primes = sorted(sieve_for_primes_to(upper_limit))
prime_check = set(primes)  # using a set to check if a number is prime is much faster in python

longest_number = 1
longest_prime = 0 
for i in range(0, len(primes)): 

    # calculate longest sequence for prime in position i
    p = primes[i]
    j = 1
    while i+j < len(primes) and p + primes[i+j] < upper_limit  :
        p += primes[i+j]

        # is the sum until this number a prime and longer than previous sum? 
        if p in prime_check and longest_number < j:
            longest_number, longest_prime = j, p

        j += 1


print(longest_prime)

