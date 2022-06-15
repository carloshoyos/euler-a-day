"""
Project Euler Problem 15
========================

Starting in the top left corner of a 2 * 2 grid, there are 6 routes
(without backtracking) to the bottom right corner.

How many routes are there through a 20 * 20 grid?
"""

import math

# A really nice relationship between counting latices and combinatorics.  
# The # of paths from (0,0) to (k,n) is equal to "the number of combinations of k objects out of k+n options".  
# Here's a more thorough explanation than what I can do in my comments: https://stemhash.com/counting-lattice-paths/
# 
# So, a simple one liner..  40!/(20! 20!)

print(int(math.factorial(40) / (math.factorial(20) * math.factorial(20) ) ) )
