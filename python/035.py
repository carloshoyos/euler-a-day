"""
Project Euler Problem 35
========================

The number, 197, is called a circular prime because all rotations of the
digits: 197, 971, and 719, are themselves prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37,
71, 73, 79, and 97.

How many circular primes are there below one million?
"""

# brute force, precompute all primes and then test for each prime, that each of its cycle are in the list. 
# converting list into set speeds up things dramatically

# profiling 
# making the list of primes a set improves performance considerably (700x faster) as the most expensive operation is checking if a number is in the set an lookups are optimized in sets.


# time for ceiling using: 
#         10^6      10^7
# set:    0.316     3.139 
# list:   210.37    2103



# calculate all primes below one million
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


primes_set = frozenset(sieve_for_primes_to(1000000))


# # first approach, loops c style
# count = 0 
# for d in primes_set: 
#     d = str(d)
#     checks = len(d)
#     db = d + d
#     for i in range(0,len(d)):
#         if int(db[i:len(d)+i]) in primes_set:
#             checks -= 1
    
#     if checks == 0: # all cycles matched prime test 
#         count +=1 
#         print(d)

# print(count)

# more concise approach 
def iscircle(x):
    global primes_set
    d = str(x)
    db = d + d
    for i in range(0,len(d)):
        if int(db[i:len(d)+i]) not in primes_set:
            return False
    return True
    

print( len([x for x in primes_set if iscircle(x)]) )