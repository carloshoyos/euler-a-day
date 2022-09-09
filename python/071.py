"""
Project Euler Problem 71
========================

Consider the fraction, n/d, where n and d are positive integers. If n < d
and HCF(n,d)=1, it is called a reduced proper fraction.

If we list the set of reduced proper fractions for d 8 in ascending order
of size, we get:

1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, 2/5, 3/7, 1/2, 4/7, 3/5, 5/8, 2/3,
                       5/7, 3/4, 4/5, 5/6, 6/7, 7/8

It can be seen that 2/5 is the fraction immediately to the left of 3/7.

By listing the set of reduced proper fractions for d 1,000,000 in
ascending order of size, find the numerator of the fraction immediately to
the left of 3/7.
"""

# approach 
# for ever denominator d, if  n/d is the closest fraction to the left of 3/7, then n = floor((3/7)*d) 
# iterate through all possible denominators and find the closest one that is not exactly the fraction 3/7
# a small hack to improve performance, if the denominator is divisible by 7, the closest fraction will be exactly 3/7.  So skip denominators % 7 == 0


target = 3/7
candidate_num = 0
candidate_frac = 0

for d in range(1,1000000):
    if d%7 == 0: continue # skip when d is a multiple of 7, as it will lead to exactly 3/7 

    num = int(d*target)
    test_frac = num/d
    if test_frac > candidate_frac:
        candidate_frac = test_frac
        candidate_num = num

print(candidate_num)
