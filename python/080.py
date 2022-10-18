"""
Project Euler Problem 80
========================

It is well known that if the square root of a natural number is not an
integer, then it is irrational. The decimal expansion of such square roots
is infinite without any repeating pattern at all.

The square root of two is 1.41421356237309504880..., and the digital sum
of the first one hundred decimal digits is 475.

For the first one hundred natural numbers, find the total of the digital
sums of the first one hundred decimal digits for all the irrational square
roots.
"""

# this one has a big gotcha..  problem refers to the sum of the first one hundred digits, e.g.  for sqr(2) = 1.414..  the sum would be 1+4+1+4... 
# I had a false start as I was adding the fractional part (the digits to the right of the period).  
# approach a: Use python decimal and setting precision for 100 digits.  I couldn't make it work at first, I thought it was a precision error, but after making approach b work, I noticed I had misread the problem, the expectation was 100 digits and not 100 decimal digits.  
# approach b: Using the property that sqr(100^2 * x) = 100 * sqrt(x) 



import math



## approach a Use python decimal and setting precision for 100 digits. 

from decimal import *
getcontext().prec = 104
running_sum = 0 
for i in range(1, 101):

    # ignore numbers that are squares
    if math.isqrt(i) ** 2 == i: continue 

    dig = str(Decimal(i).sqrt())
    running_sum += sum([int(d) for d in dig[0:101] if d != '.' ])

print(running_sum)


## approach b -  use the property that sqr(100^100 * x) = 100 * sqrt(x)
## since we only care about 100 digits, we can calculate the integer square root and count the digits before the decimal point.
running_sum = 0 
for i in range(1, 101):

    # ignore numbers that are squares
    if math.isqrt(i) ** 2 == i: continue 

    dig = str(math.isqrt(i * 100**100))
    try:
        running_sum += sum([int(d) for d in dig[0:100] ])
    except: print(dig)

print(running_sum)
