"""
Project Euler Problem 12
========================

The sequence of triangle numbers is generated by adding the natural
numbers. So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 =
28. The first ten terms would be:

                 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

Let us list the factors of the first seven triangle numbers:

   1: 1
   3: 1,3
   6: 1,2,3,6
  10: 1,2,5,10
  15: 1,3,5,15
  21: 1,3,7,21
  28: 1,2,4,7,14,28

We can see that 28 is the first triangle number to have over five
divisors.

What is the value of the first triangle number to have over five hundred
divisors?
"""


# An initial brute force approach is to factorize each triangle number, e.g. t = p1**n1 * p2**n2 ...  
# all factors will be the permutations of the exponents from 0 to n1, n2, n3...   so count of unique factors is (n1+1)*... *(ni+1)
# my first approach was a bit slow, as I factor each number by dividing by all prime numbers 
# for a faster approach I should generate all prime numbers to a reasonable ceiling with a sieve.  

from math import isqrt


def prime_generator(ceiling):
    i = 3
    primes = []  # will store all primes above 2 in this array to test future candidates 
    yield 2
    while i <= ceiling:
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


def divisor_exponents_primes(x):
    '''
    returns prime factorization of number x in the format [(p1, n1), (p2, n2) ... )] where x = p1**n1 * p2**n2 ... 
    '''
    originalNumber = x
    expList = []
    count = 0
    divisors = prime_generator(x)
    divisor = 1 #next(divisors)
    
    try:
      while divisor <= x:
          divisor = next(divisors)
          # print("trying divisor", divisor, "on", x)
          while x % divisor == 0:
              x = x/divisor
              count += 1
          if count != 0:
              expList.append((divisor,count))
          count = 0
    except:
      print("exception with ", originalNumber)
    return expList
    #return reduce(lambda x, y: x * y, expList, 1)

def count_factors(x):
  '''
  returns total number of factors for x. 
  '''
  # if x = p1**n1 * p2**n2 ...  pi**ni,  then the count of factors is (n1+1)*... *(ni+1)
  prod = 1
  for prime, exp in divisor_exponents_primes(x):
    prod *= (exp+1)
  return(prod)


n = 1
triangular = 0

while True:
    triangular += n
    n += 1
    if count_factors(triangular) > 500:
        break

print(triangular)
