"""
Project Euler Problem 63
========================

The 5-digit number, 16807=7^5, is also a fifth power. Similarly, the
9-digit number, 134217728=8^9, is a ninth power.

How many n-digit positive integers exist which are also an nth power?
"""
import itertools as it

# a brute force approach will work but need to reduce the solution space. 

# to estimate boundaries,  consider x^y:

# 1- only test x < 10: 
#   when x == 10, 10^y will always have y+1 digits. Numbers greater than 10 are even larger, 
#   thus we don't have to look at x^y for x >= 10. 
# 2- test incrementally starting with y =1, and stop when x^y has less than y digits: 
#   when testing for x < 10, if x^y has less digits than y, then x^(y+1) will have less than y+1 digits, 
#   because we multiply x^y (<y digits) by x (which is <10) 

# with the aove constrains, the code is straightforward: 


valid_numbers = 0 # counter

for base in range(1, 10):
    for exp in it.count(1):
        number_len = len(str(base**exp)) 
        if number_len == exp:
            valid_numbers += 1
        if number_len < exp:
            break

print(valid_numbers)

# pythonic way, had to hard code the exp ceiling 
print(sum(1
		for base in range(1, 10)
		for exp in range(1, 25)
		if len(str(base**exp)) == exp)
)