"""
Project Euler Problem 32
========================

We shall say that an n-digit number is pandigital if it makes use of all
the digits 1 to n exactly once; for example, the 5-digit number, 15234,
is 1 through 5 pandigital.

The product 7254 is unusual, as the identity, 39 * 186 = 7254, containing
multiplicand, multiplier, and product is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product
identity can be written as a 1 through 9 pandigital.

HINT: Some products can be obtained in more than one way so be sure to
only include it once in your sum.
"""


# A simple brute force approach once I can estimate a ceiling for the result:  
# We can easily see the result is < 10000 (5 digits), because there would be 4 digits left for the product part, and the product would be less than 99 * 99 = 9801 (four digits) 


from math import isqrt


# checks if number i has a pandigital product by checking each of its divisors 
def has_pandigital_product(i):
    for div in range(1, isqrt(i)+1):    # only need to check from 2 to square root.
        if i % div == 0:
            if ''.join(sorted(str(div) + str(i//div) + str(i) )) == '123456789':
                #print(div, i//div, i )  # this to see all the pandigital values
                return True
    return False


sum = 0
for i in range(100, 10000):
    if has_pandigital_product(i):
        sum += i
print(sum)