"""
Project Euler Problem 60
========================

The primes 3, 7, 109, and 673, are quite remarkable. By taking any two
primes and concatenating them in any order the result will always be
prime. For example, taking 7 and 109, both 7109 and 1097 are prime. The
sum of these four primes, 792, represents the lowest sum for a set of four
primes with this property.

Find the lowest sum for a set of five primes for which any two primes
concatenate to produce another prime.
"""


# approach:  
# 1) create a list of all primes (using sieve) and use it to check efficiently if two primes p1, p2 are stackable primes (stackable means p1.p2 and p2.p1 are primes)
# 2) Create a list for each prime p1, of all primes p2 that are stackable primes. 
# 3) Start building up longer chains by iterating throuhg each combination (p1, p2) above, and findinging valid p3 where p1, p2 and p3 are stackable primes
# 4) Continue recursively until length is chain_length
# note since 
from functools import lru_cache
import itertools
import time 


# to make search efficient, constrain the solution space. 
# Assume the max prime in the chain is less than  max_prime_size
max_primes_length = 8       # this is the max combined size of p1.p2 that we will test for. 
chain_length = 5            # max chain length to search for. 

max_primes = 10**max_primes_length
max_prime_size = 10**(max_primes_length//2)
 

min_sum = max_primes

def get_set_primes_to(n):
    size = n//2
    prime_list = [x if (x%2 != 0) or (x == 2) else 0 for x in range(0,n+1)]

    sqrt_n = int(n**0.5)  # only sieve until square root of max value 
    for i in range(3,sqrt_n+1):
        if prime_list[i]:  # remove all factors of a prime number
            prime_list[i*2::i] = [0] * (n // i - 1)  # mark as zero for deletion 
  
    # remove non primes 
    prime_list = {x for x in prime_list if x > 1}
    return prime_list

# this simple function only works for prime < max prime calculated in our sieve. Validating using an assertion.
def is_prime(prime):
    assert prime < max_primes
    return prime in prime_list

# faster way to cache this
@lru_cache(maxsize=None)
def is_swapprime(p1, p2):
    """return true if both concat of p1.p2 and p2.p1 are prime"""
    return is_prime(int(str(p1)+str(p2))) and is_prime(int(str(p2)+str(p1))) 


start = time.time()

prime_list = get_set_primes_to(max_primes)
test_primes =  sorted([x for x in prime_list if x < max_prime_size])

#print(f"time to generate primes", time.time() - start)       


# fill stackable prime list, for example for 3, the  entry is (3, [7, 11, 17, 31...]) where all numbers in this list are stackable primes with 3
stackable_list= dict((p,[]) for p in test_primes)
for p1, p2 in itertools.combinations(test_primes,2) :
    if len(str(p1)+str(p2))<8 and is_swapprime(p1, p2):
        stackable_list[p1].append(p2)

#print(f"time to generate pairs", time.time() - start)       

# finally recursively test and generate longer chains of stackable primes until we get to five 
def test_chain(chain,cur):
    global min_sum
    if len(chain)==chain_length :
        min_sum = min(sum(chain), min_sum)
        #print(sum(chain),chain)
        return 0
    for i in range(cur+1,len(test_primes)):
        if all(is_swapprime(test_primes[i],p) for p in chain) : test_chain(chain+[test_primes[i]],i)




for i in range(len(test_primes)):
    test_chain([test_primes[i]],i)

print(min_sum)
#print("min sum", min_sum, f"time to test chains", time.time() - start)       

