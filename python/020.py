"""
Project Euler Problem 20
========================

n! means n * (n - 1) * ... * 3 * 2 * 1

Find the sum of the digits in the number 100!
"""

# python makes this so easy..   one of the easiest problems in this challenge. 

import math
print(sum( int(x) for x in str(math.factorial(100)) ))