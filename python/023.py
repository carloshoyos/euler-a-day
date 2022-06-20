"""
Project Euler Problem 23
========================

A perfect number is a number for which the sum of its proper divisors is
exactly equal to the number. For example, the sum of the proper divisors
of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect
number.

A number whose proper divisors are less than the number is called
deficient and a number whose proper divisors exceed the number is called
abundant.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the
smallest number that can be written as the sum of two abundant numbers is
24. By mathematical analysis, it can be shown that all integers greater
than 28123 can be written as the sum of two abundant numbers. However,
this upper limit cannot be reduced any further by analysis even though it
is known that the greatest number that cannot be expressed as the sum of
two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as the
sum of two abundant numbers.
"""

# reusing problen 21 to calculate all abundant numbers quickly.  
# then iterate and remove all the digits that can be writen as the sum of two abundant numbers

ceiling = 28123

def getDivisorsSum(ceiling): 
	# Returns a list of all divisors for numbers up to ceiling 
    # for example, position 12 has 16  ( 1 + 2 + 3 + 4 + 6 ) 
    divisors = [1 for i in range(0, ceiling+1)] 
    for x in range(2, ceiling+1):
        for j in range(x * 2, ceiling+1, x):
            divisors[j] += x
    return divisors

# get a list of abundant #s 
abundant = [i for (i,x) in enumerate(getDivisorsSum(ceiling)) if i < x and i >0 ]

# calculate all numbers < 28123 that can be expressed as sum of 2 abundables 
abundsum = {x for x in range(1, ceiling)}

for x in abundant:
    for y in abundant:
        abundsum.discard(x+y)

print(sum(abundsum))
