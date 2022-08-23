"""
Project Euler Problem 64
========================

All square roots are periodic when written as continued fractions and can
be written in the form:

N = a[0] +            1
           a[1] +         1
                  a[2] +     1
                         a[3] + ...

For example, let us consider 23:

23 = 4 + 23 -- 4 = 4 +  1  = 4 +  1     1     1 +  23 - 3
                                      23--4          7

If we continue we would get the following expansion:

23 = 4 +          1
         1 +        1
             3 +      1
                 1 +    1
                     8 + ...

The process can be summarised as follows:

a[0] = 4,     1    =   23+4    = 1 +  23--3
            23--4        7              7
a[1] = 1,     7    =  7(23+3)  = 3 +  23--3
            23--3       14              2
a[2] = 3,     2    =  2(23+3)  = 1 +  23--4
            23--3       14              7
a[3] = 1,     7    =  7(23+4)  = 8 +  23--4
            23--4        7
a[4] = 8,     1    =   23+4    = 1 +  23--3
            23--4        7              7
a[5] = 1,     7    =  7(23+3)  = 3 +  23--3
            23--3       14              2
a[6] = 3,     2    =  2(23+3)  = 1 +  23--4
            23--3       14              7
a[7] = 1,     7    =  7(23+4)  = 8 +  23--4
            23--4        7

It can be seen that the sequence is repeating. For conciseness, we use the
notation 23 = [4;(1,3,1,8)], to indicate that the block (1,3,1,8) repeats
indefinitely.

The first ten continued fraction representations of (irrational) square
roots are:

2=[1;(2)], period=1
3=[1;(1,2)], period=2
5=[2;(4)], period=1
6=[2;(2,4)], period=2
7=[2;(1,1,1,4)], period=4
8=[2;(1,4)], period=2
10=[3;(6)], period=1
11=[3;(3,6)], period=2
12= [3;(2,6)], period=2
13=[3;(1,1,1,1,6)], period=5

Exactly four continued fractions, for N 13, have an odd period.

How many continued fractions for N 10000 have an odd period?
"""


# loved learning about continued fractions, 
# many interesting features, a great resource is here:  https://r-knott.surrey.ac.uk/Fibonacci/cfINTRO.html
# algorithm from wikipedia:  https://en.wikipedia.org/wiki/Methods_of_computing_square_roots#Continued_fraction_expansion

# I tried at first to find the formula with pen and paper, and it took me a few days to something that was working. 
# implemented based on this: https://web.archive.org/web/20151221205104/http://web.math.princeton.edu/mathlab/jr02fall/Periodicity/mariusjp.pdf


# as for the actual problem, the process is a bit tedious, but implementable: 
#    - the first digit a(0)  is the int of the number square root. then this equations : 
#   
#  sqrt(n) = a + x 
#  n = a^2 + 2ax + x^2 
#  n-a^2  =  x (2a - x)

# from above we can calculate x = (n - aˆ2) / (2a - x)

import math


# return length of period or 0 for perfect squares
# continuedFractionforSqrt(2)  returns a pair (1, [2]).  Period is the length of element [1]
def continuedFractionforSqrt(n):

    #closest perfect square to the square root
    root = a0 = math.isqrt(n)

    cont_fraction = (a0, [])

    # return if n is a perfect square
    if a0 * a0 == n: 
        return cont_fraction


    numerator   = 0 
    denominator = 1  
    period = 0

    while True: 
        numerator   = denominator * a0 - numerator
        denominator = (n - numerator * numerator) // denominator
        a0 = (root + numerator) // denominator


        # iterate until we see the same triplet (a, numerator, denominator) a second time
        # first iteration we store the triple
        # after that we check if next triplet has been seen before
        if period == 0:
            a,den,num = a0, denominator, numerator
        elif (a,den,num) == (a0, denominator, numerator): # if we see the same triplet again, we hit a period
            break

        cont_fraction[1].append(a0)   
        period += 1
    return cont_fraction



print(sum([1 for x in range(2,10001) if (len(continuedFractionforSqrt(x)[1]) %2 == 1) ]))

