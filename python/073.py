"""
Project Euler Problem 73
========================

Consider the fraction, n/d, where n and d are positive integers. If n < d
and HCF(n,d)=1, it is called a reduced proper fraction.

If we list the set of reduced proper fractions for d 8 in ascending order
of size, we get:

1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, 2/5, 3/7, 1/2, 4/7, 3/5, 5/8, 2/3,
                       5/7, 3/4, 4/5, 5/6, 6/7, 7/8

It can be seen that there are 3 fractions between 1/3 and 1/2.

How many fractions lie between 1/3 and 1/2 in the sorted set of reduced
proper fractions for d 10,000?
"""

# approach a) try all possible combinations by finding primes that divide every number in 1-10^6 and counting those numbers that don't have the same primes)
# approach b) same but in a pythonic way and not calculating reduced fractions, just doing the division and finding unique values 
# approach b) this is called the farey sequence... rabbit hole
# approach c) the stern-brocot tree, another rabbit hole of fascinating information 



# approach a), helper function
# # return a list where l[n] = set(p1, p2) of all primes that divide n
def sieve_for_div_primes(n):

    # calculate all primes 
    size = n//2
    prime_list = [x if (x%2 != 0) or (x == 2) else 0 for x in range(0,n+1)]

    sqrt_n = int(n**0.5)  # only sieve until square root of max value 
    for i in range(3,sqrt_n+1):
        if prime_list[i]:  # remove all factors of a prime number
            prime_list[i*2::i] = [0] * (n // i - 1)  # mark as zero for deletion 
 
    # remove non primes 
    prime_list = [x for x in prime_list if x > 1]

    # cal
    prime_factors = [set() for x in range(0,n+1) ]
    for i in prime_list:
           for j in range(i,n+1, i):
                prime_factors[j].add(i)
                #print(f"adding {i} to {j}")


    return prime_factors

upper_limit = 12000 

import time

st = time.time()

# uncomment this to run approach a, but it will not run fast O(n^2)
total = 0
divs = sieve_for_div_primes(upper_limit)
for i in range (1, upper_limit+1):
    for j in range(i+1, upper_limit+1):
        if bool(divs[i] & divs[j]) == False:
            if 1/3 < i/j and i/j < 0.5:
                total += 1
print(total)
print("time", time.time()-st)



# uncomment this to run approach b, but it will not run fast O(n^2)

st = time.time()
print(
len(set([float(a)/b for a in range(1,upper_limit+1) for b in range(a+1,upper_limit+1) if float(a)/b > 1.0/3 if float(a)/b < .5 ]))
)
print("time", time.time()-st)
