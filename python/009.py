"""
Project Euler Problem 9
=======================

A Pythagorean triplet is a set of three natural numbers, a < b < c, for
which,
                             a^2 + b^2 = c^2

For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""


## the simple brute force approach was super easy, completed in < 2 minutes.  Took many freedoms like knowing that there is one solution (so function knows there is a guaranteed return). 
## A way to improve this is with the Pythagorean triplet formula a = (m^2-1), b = (2m), and c = (m^2+1) 

## performance
#  tbd once I implement an alternative using triplet formula.  


# Brute force  / iterate through all options.   Capping the outer loop at max//2 although it is probably lower.  
def product_firstpythonaddsto(max):
    for a in range(2,max//2):
        for b in range(2, max-a):
            c = max-a-b
            if (a**2 + b**2 == c**2):
                #print(a,b,c, a*b*c)
                return(a*b*c)

print(product_firstpythonaddsto(1000))