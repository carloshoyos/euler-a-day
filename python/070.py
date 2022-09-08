"""
Project Euler Problem 70
========================

Euler's Totient function, f(n) [sometimes called the phi function], is
used to determine the number of positive numbers less than or equal to n
which are relatively prime to n. For example, as 1, 2, 4, 5, 7, and 8, are
all less than nine and relatively prime to nine, f(9)=6.
The number 1 is considered to be relatively prime to every positive
number, so f(1)=1.

Interestingly, f(87109)=79180, and it can be seen that 87109 is a
permutation of 79180.

Find the value of n, 1 < n < 10^7, for which f(n) is a permutation of n
and the ratio n/f(n) produces a minimum.
"""

# approach a) straightforward reusing problem 69.  calculate phi function using a sieve and then find minimum n/phi for that array. 


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

phi = totient_sieve(10000000)

print(min( [ x for x in range(2,10000001) if sorted(str(x)) == sorted(str(int(phi[x-2])))],  key = lambda x: x / phi[x-2] ))


