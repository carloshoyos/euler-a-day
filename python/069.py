"""
Project Euler Problem 69
========================

Euler's Totient function, f(n) [sometimes called the phi function], is
used to determine the number of numbers less than n which are relatively
prime to n. For example, as 1, 2, 4, 5, 7, and 8, are all less than nine
and relatively prime to nine, f(9)=6.

+------------------------------------------+
| n  | Relatively Prime | f(n) | n/f(n)    |
|----+------------------+------+-----------|
| 2  | 1                | 1    | 2         |
|----+------------------+------+-----------|
| 3  | 1,2              | 2    | 1.5       |
|----+------------------+------+-----------|
| 4  | 1,3              | 2    | 2         |
|----+------------------+------+-----------|
| 5  | 1,2,3,4          | 4    | 1.25      |
|----+------------------+------+-----------|
| 6  | 1,5              | 2    | 3         |
|----+------------------+------+-----------|
| 7  | 1,2,3,4,5,6      | 6    | 1.1666... |
|----+------------------+------+-----------|
| 8  | 1,3,5,7          | 4    | 2         |
|----+------------------+------+-----------|
| 9  | 1,2,4,5,7,8      | 6    | 1.5       |
|----+------------------+------+-----------|
| 10 | 1,3,7,9          | 4    | 2.5       |
+------------------------------------------+

It can be seen that n=6 produces a maximum n/f(n) for n 10.

Find the value of n 1,000,000 for which n/f(n) is a maximum.
"""


# totient function. 
# many approaches: 
# a) naive, for each number x less than n, calculate gcd(x, n) and count those where gcd(x, n) > 1  (this times out)
# b) use euler's formula that phi(n) = n * prod(1- 1/p) where p are primes that divide n.  
# c) since we want to minimize f(n), the number with the least coprimes will be the one that has is divisible by all primes p1*p2*p3 and below upper range
# d) use can use the idea of the prime sieve to create a phi sieve

# approach a) ----------------------------------------------------
# simple implementation of gcd  
def gcd(a, b):
 
    if (a == 0):
        return b
    return gcd(b % a, a)

def phi_naive(n):
    return sum([1 for x in range(1,n) if gcd(n, x) == 1 ])

## uncomment this to run approach a
# print(max(range(2,1000001), key= phi_naive))


# approach b -----------------------------------------------------
# using implementation from https://www.geeksforgeeks.org/eulers-totient-function/ which has o(sqrt(n)) complexity
def phi_eulereq(n):
    # Initialize result as n
    result = n
 
    # Consider all prime factors
    # of n and subtract their
    # multiples from result
    p = 2;
    while(p * p <= n):
         
        # Check if p is a
        # prime factor.
        if (n % p == 0):
             
            # If yes, then
            # update n and result
            while (n % p == 0):
                n = int(n / p);
            result -= int(result / p);
        p += 1;
 
    # If n has a prime factor
    # greater than sqrt(n)
    # (There can be at-most
    # one such prime factor)
    if (n > 1):
        result -= int(result / n);
    return result;

def totient_ratio(n):
    return n / phi_eulereq(n)

## uncomment this to run approach b
# print(max(range(2,1000001), key= totient_ratio))


# approach c) -------------------------------------------------------
# since we want to maximize n / phi(n), using euler's product formula:
# n /phi(n) = n / [ n * prod(1- 1/p) ]
#           = 1 / prod( (p-1)/ p)

# since p-1 / p < 1, the more prime numbers in this product the smaller the it will be and thus 1/ prod will be larger
# so the bigger the multiplication of p1.p2.p3.p4 the higher it will be, we just need to find the largest multiplication of first primes lower than upper bound

import math
# check if number is prime (via division)
def isPrime(x):

    # get trivial cases out of the way 
    if x == 2 or x == 3:
        return True
    elif x % 2 == 0 or x <= 1:
        return False
    else:
        for i in range(3, math.isqrt(x) + 1, 2):
            if x % i == 0:
                return False
        return True

def get_max_totient_ratio(upper_limit):

    result =1
    prime = 2
    while True:
        if isPrime(prime):
            if result * prime > upper_limit:
                return result
            result *= prime
        prime += 1


## uncomment this to run approach c
print(get_max_totient_ratio(1000001))



# approach 4 - sieve. Use euler multiplication formula to multiply every number n by (1 - 1/p) for all p prime dividers of n. 
# creates an array with all the phi values
def totient_sieve(upper_limit):
    try:
        phi = [i for i in range(2, upper_limit+2)]

        for i, val in enumerate(phi):
            i += 1

            if i+1==val:  # hasn't been evaluated, must be prime
                    num1 = val -1
                    num2 = val
                    # multiply all multiples of val by (1  -1 /  val) == ( (val -1) / val )
                    for j in range(i-1, upper_limit, i+1): 
                        phi[j] *= (val-1) / val
                        if j+i +2 > upper_limit: 
                            break
    except:
        print("error with j", j)
    return phi

## uncomment this to run approach d
# phi_sieve = totient_sieve(1000001)
# print(max(range(2,1000001), key= lambda x: x/phi_sieve[x-2]))


