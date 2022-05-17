"""
Project Euler Problem 4
=======================

A palindromic number reads the same both ways. The largest palindrome made
from the product of two 2-digit numbers is 9009 = 91 * 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

# another easy one...  brute force all pairs and find the max product that is palindromde. 
# two functions, one (a) with nested loops, the other (b) more pythonic.  
# note that for 3 digit numbers this works well (0.2 secs to run), but this method doesn't scale.  For 4 digits the time is 26 seconds. 


# Performance
# pythonic method is ~10% slower. 
# 

# a) brute force all solutions.  a simpler optimization, compute only pairs whene a <= b to remove duplicate pairs (since a * b == b * a) 
def compute():
    answer = 0  # assuming there is an answer, otherwise it will return 0
    for a in range(101, 1000):
        for b in range(a, 1000):
            if str(a * b) == str(a * b)[ : : -1] and a * b > answer:
                answer = a * b
    
    return str(answer)


# b) Same as above but a more "pythonic" solution.  The performance between these two is the same, but for much larger numbers 
def compute_pythonic():
	answer = max(i * j
		for i in range(101, 1000)
		for j in range(i, 1000)
		if str(i * j) == str(i * j)[ : : -1])
	return str(answer)


if __name__ == "__main__":
    # print(compute_pythonic())
    print(compute())
