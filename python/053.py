"""
Project Euler Problem 53
========================

There are exactly ten ways of selecting three from five, 12345:

           123, 124, 125, 134, 135, 145, 234, 235, 245, and 345

In combinatorics, we use the notation, nCr(5,3) = 10.

In general,

nCr(n,r) = n!/(r!(n-r)!), where r =< n, n! = n * (n1) * ... * 3 * 2 * 1,
and 0! = 1.

It is not until n = 23, that a value exceeds one-million: nCr(23,10) =
1144066.

How many values of nCr(n,r), for 1 =< n =< 100, are greater than one-million?
"""


# approach 1, brute force.  the numbers might be too large, but python handles it like a champ. 
# approach 2 -  use pascal triangle as it calculates each combination (binomial) number. 
# a few interesting formulas: 
#   -  nCr(n,m) = nCr(n-1,m-1) + nCr(n-1,m).  Once we know that a number hits 10^6, all numbers derived will be 1 million too
#   -  C(line, i) = C(line, i-1) * (line - i + 1) / i    
#   store the Pascal’s triangle in a matrix then the value of nCr will be the value of the cell at nth row and rth column. 

# Performance: python handles 100 rows fine with both brute force and formula
# by 500 it is struggling though
# n     formula     brute force
# 100   
# 500 


import math 
def calculateCombGreaterThan_Bruteforce(upper_limit = 1000000, n=100):
    greater_count = 0 # greater than a million 
    for line in range(1, n+1):
        for j in range(1, line+1):
            C = math.factorial(line) / (math.factorial(j) * math.factorial(line-j))
    

            if C > upper_limit:
                greater_count += 1
    return greater_count


 
def calculateCombGreaterThan_formula(upper_limit = 1000000, n=100):


    greater_count = 0  
    for line in range(1, n+2): # combinatorics starts on line 2  of pascal triangle, so have to end in n+1

        # first element is always 1
        C = 1
        for j in range(1, line+1):

            C = C * (line - j) // j  # using Binomial Coefficient

            if C > upper_limit:
                greater_count += 1
    return greater_count

print(calculateCombGreaterThan_formula(1000000, 100))
#print(calculateCombGreaterThan_Bruteforce(1000000, 100))