"""
Project Euler Problem 51
========================

By replacing the 1st digit of *57, it turns out that six of the possible
values: 157, 257, 457, 557, 757, and 857, are all prime.

By replacing the 3rd and 4th digits of 56**3 with the same digit, this
5-digit number is the first example having seven primes, yielding the
family: 56003, 56113, 56333, 56443, 56663, 56773, and 56993. Consequently
56003, being the first member of this family, is the smallest prime with
this property.

Find the smallest prime which, by replacing part of the number (not
necessarily adjacent digits) with the same digit, is part of an eight
prime value family.
"""


# masks! 
# approach 1: Bruteforce 
# for a given number, calculate all of its possible masks (2^len(number)-1) and replace the mask with 0
# for example for 123, there are 7 masks..  .23, 1.3, 12., .2., ..3, 1.., ...  with the last one can be ignored 
# for each mask, do a replacement of . to each number 0-9 and see which are primes for a total count. 
# Careful with edge case when the last digit (to the left) is a mask, you can't replace with 0 

# Approach 2: optimizations
#   don't test all numbers..  
#       a) start only with prime numbers that have repeated numbers.  Test replacing only the repeated numbers
#       b) given we look for at least 8 chains, one of 0, 1, 2 must be a valid replacement replaced to reach family size 8 in total. 
#   don't test all masks... for a chain >7 expect
#       masks with only 1,2 or 4 replacements won't produce 8+ results, as at least three of them will be divisible by 3 (because of sum of it's digits) so total family size < 8

import time


# generate all primes
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


# returns a list with the digits for num, but the values where mask == 1 (in binary), are ''
def maskNumber(num, mask):
    return [d * ((mask >> i) & 1) for (i, d) in enumerate(str(num))]

# first approach, brute force, test all prime numbers.
def calculateLongestChainBruteForce(chainSize = 8, maxPrime = 1000000):

    primes = sieve_for_primes_to(maxPrime)
    primes_to_check = set(primes)

    max_group_size = 0
    min_prime = 0
    for n in primes:

        for mask in range(1, 2 ** len(str(n)) - 1):
            masked_number = maskNumber(n, mask)
            start = 0 if masked_number[0] else 1    # if the mask includes the first right digit, don't replace
            
            primes_for_mask = []
            for replace in range(start, 10):
                r = int("".join([x if x else str(replace) for x in masked_number]))
                if r in primes_to_check:
                    primes_for_mask.append(r)


            if len(primes_for_mask) > max_group_size:
                max_group_size = len(primes_for_mask)
                min_prime = min(primes_for_mask)

                #print("found new max {} for {} using mask {} {}".format(max_group_size, primes_for_mask, mask, masked_number))
                
                if chainSize == max_group_size:
                    return min_prime

# second approach. Test only numbers with 3,6,9 variable patterns and change only first 0,1,2  digits              
def calculateLongestChainOptimized(chainSize = 8, maxPrime = 1000000):

    primes = sieve_for_primes_to(maxPrime)
    primes_to_check = set(primes)

    max_group_size = 0
    min_prime = 0

    for n in primes:
        if n <100: continue     # skip 1 and 2 digit primes to avoid edge case

        # check that there are repeats of the numbers 0 or 1 or 2, and those repeats come in groups of 3 
        n = str(n)
        for d in '012':
            if n.count(d)  in (3,6,9): 

                # check how many are primes when replacing digit d  with 0 to 9, ? 
                primes_for_mask = []
                nonprimes = 0 

                # don't replace 0 if the first digit is a wild card
                start = 1 if n[0]==d else 0

                for replace in range(start, 10):
                    testprime = int(n.replace(d, str(replace)))
                    if testprime in primes_to_check:
                            primes_for_mask.append(testprime)

                # did we find a new larger chain? 
                if len(primes_for_mask) > max_group_size:
                    max_group_size = len(primes_for_mask)
                    min_prime = min(primes_for_mask)

                    #print("found new max {} for {} ".format(max_group_size, primes_for_mask))
                    
                    if chainSize == max_group_size:
                        return min_prime

#start = time.time()
print(calculateLongestChainOptimized())

#print(time.time() - start)
#print(calculateLongestChainBruteForce())
#print(time.time() - start)