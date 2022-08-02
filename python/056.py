"""
Project Euler Problem 56
========================

A googol (10^100) is a massive number: one followed by one-hundred zeros;
100^100 is almost unimaginably large: one followed by two-hundred zeros.
Despite their size, the sum of the digits in each number is only 1.

Considering natural numbers of the form, a^b, where a, b < 100, what is
the maximum digital sum?
"""


# approach 1: brute force, python is cool that this took very little time to run

# iterative way 
dsum = 0
for a in range(1,100):
    for b in range(1,100):
        dsum = max(dsum, sum([int(d) for d in str(a ** b)]))

print(dsum)


# more pythonic way, assuming we don't need to check smaller powers (starts at 80)
print(max( 
 [ sum( [ int(d) for d in str( a ** b ) ] ) for a in range( 80, 100 ) for b in range( 80, 100 ) ] 
))