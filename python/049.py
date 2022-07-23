"""
Project Euler Problem 49
========================

The arithmetic sequence, 1487, 4817, 8147, in which each of the terms
increases by 3330, is unusual in two ways: (i) each of the three terms are
prime, and, (ii) each of the 4-digit numbers are permutations of one
another.

There are no arithmetic sequences made up of three 1-, 2-, or 3-digit
primes, exhibiting this property, but there is one other 4-digit
increasing sequence.

What 12-digit number do you form by concatenating the three terms in this
sequence?
"""

# using sieve (problem 7) to calculate all the 4 digit primes. 
# then iterate through them, and find next prime in sequence that matches conditions above.  
# print first result  

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

def has_same_digits(i,j):
	return sorted(str(i)) == sorted(str(j))



def calculate_sequence():
    primes = sorted(sieve_for_primes_to(10000))

    for i in primes:
        if i <1000 or i == 1487: continue  #  only evaluate 4 digit primes and skip the sequence that starts with 1487


        for j in primes:
            if i !=j \
                and has_same_digits(i, j) \
                and 2*j-i in primes \
                and has_same_digits(i, 2*j-i):

                return str(i) + str(j) + str(2*j-i )

print(calculate_sequence())