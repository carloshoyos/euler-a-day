"""
Project Euler Problem 37
========================

The number 3797 has an interesting property. Being prime itself, it is
possible to continuously remove digits from left to right, and remain
prime at each stage: 3797, 797, 97, and 7. Similarly we can work from
right to left: 3797, 379, 37, and 3.

Find the sum of the only eleven primes that are both truncatable from left
to right and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
"""

# to speed this up, pre calculate  primes with a sieve. 
# Also, number can't have any even or ==5 digits b/c of left to right truncation makes an even number.


import itertools

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
    return set(prime_list)


sieve_size = 1000000
primes = sieve_for_primes_to(sieve_size)

def isPrime(n): 
  global primes, sieve_size

  # in case our initial estimation for the sieve wasn't large enough we recalculate.
  if n > sieve_size:
    sieve_size *= 2
    primes = sieve_for_primes_to(sieve_size)
    
  return n in primes

def is_truncatable_prime(n):

    # test if prime 
    if not isPrime(n): return False

	# test if left truncatable
    i = 10
    while i <= n:
        if not isPrime(n % i):
            return False
        i *= 10
	
	# test if right truncatable
    while n > 0:
        if not isPrime(n):
            return False
        n //= 10
    
    return True


truncprimes = set()


for i in itertools.count(11, step=2):
    if is_truncatable_prime(i):
        truncprimes.add(i)  
        if len(truncprimes) > 10: 
            break 
print(sum(truncprimes))