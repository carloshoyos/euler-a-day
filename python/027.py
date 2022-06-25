"""
Project Euler Problem 27
========================

Euler published the remarkable quadratic formula:

                               n^2 + n + 41

It turns out that the formula will produce 40 primes for the consecutive
values n = 0 to 39. However, when n = 40, 40^2 + 40 + 41 = 40(40 + 1) + 41
is divisible by 41, and certainly when n = 41, 41^2 + 41 + 41 is clearly
divisible by 41.

Using computers, the incredible formula  n^2 - 79n + 1601 was discovered,
which produces 80 primes for the consecutive values n = 0 to 79. The
product of the coefficients, 79 and 1601, is 126479.

Considering quadratics of the form:

  n^2 + an + b, where |a| < 1000 and |b| < 1000

                              where |n| is the modulus/absolute value of n
                                               e.g. |11| = 11 and |-4| = 4

Find the product of the coefficients, a and b, for the quadrati
expression that produces the maximum number of primes for consecutive
values of n, starting with n = 0.
"""
# start with simplest brute force approach, calculate for the 2000*2000 posible polynomials how many primes there are when evaluated with n = 0,1,2...
# reusing sieve formula from problem 7 to make performance faster. 
# A simple optimization, notice that b has to be odd, which reduces the # of calculations and time to run by 25%.

# some research after solving this. Prime generating function history https://mathworld.wolfram.com/Prime-GeneratingPolynomial.html


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
    return prime_list


primes = sieve_for_primes_to(10000)

def isPrime(n): 
  global primes

  # in case our initial estimation for the sieve wasn't large enough we recalculate.
  if n > primes[-1]:
    primes = sieve_for_primes_to(2*n)
    
  return n in primes


def evalPolynomial(n,a,b):
  return n**2 + a*n + b


limit = 1000 # this should be even as we iterate over odd numbers
max_primes = -1
max_prod = 0

for a in range(-limit+1, limit):
  for b in range(-limit+1, limit, 2): # note, b has to be odd otherwise when n and b are even the result is div by 2
    n = 0
    while isPrime(evalPolynomial(n,a,b)):
      n += 1
    
    if (max_primes < n):
      max_primes = n
      max_prod = a * b
      #print('new max', a,b, max_primes, max_prod)

print(max_prod)