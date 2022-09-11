"""
Project Euler Problem 72
========================

Consider the fraction, n/d, where n and d are positive integers. If n < d
and HCF(n,d)=1, it is called a reduced proper fraction.

If we list the set of reduced proper fractions for d 8 in ascending order
of size, we get:

1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, 2/5, 3/7, 1/2, 4/7, 3/5, 5/8, 2/3,
                       5/7, 3/4, 4/5, 5/6, 6/7, 7/8

It can be seen that there are 21 elements in this set.

How many elements would be contained in the set of reduced proper
fractions for d 1,000,000?
"""


# we are looking for the set (n,d) where HCF(n,d)=1, d,n in [2,10^6] and n < d. 

# approach a) try all possible combinations by finding primes that divide every number in 1-10^6 and counting those numbers that don't have the same primes)
# approach b) connecting dots, since phi(d) is the count of all fractions n/d that are reduced proper fraction, so we can sum all values of phi(d) for the range 1<d<1000000


# approach a) ------  note this is too slow and had to be scratched
# return a list where l[n] = set(p1, p2) of all primes that divide n
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

upper_limit = 1000000


## uncomment this to run approach a, but it will not run fast O(n^2)
# total = 0
# divs = sieve_for_div_primes(upper_limit)
# for i in range (1, upper_limit+1):
#     for j in range(i+1, upper_limit+1):
#         if bool(divs[i] & divs[j]) == False:
#             total += 1
# print("total:", total)


#####---  approach b 

# index is off by 2,  phi[0] == euler value for 2
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

totients = totient_sieve(upper_limit)
print(int(sum([totients[x] for x in range(0,upper_limit-1)])))