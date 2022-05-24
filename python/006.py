"""
Project Euler Problem 6
=======================

The sum of the squares of the first ten natural numbers is,
                       1^2 + 2^2 + ... + 10^2 = 385

The square of the sum of the first ten natural numbers is,
                    (1 + 2 + ... + 10)^2 = 55^2 = 3025

Hence the difference between the sum of the squares of the first ten
natural numbers and the square of the sum is 3025 - 385 = 2640.

Find the difference between the sum of the squares of the first one
hundred natural numbers and the square of the sum.
"""

## given how fast computers are, this is trivial to implement by just iterating and calculating.  
## we know the formula for the sum of digits from challenge 1, and the sum of squares is [n(n+1)(2n+1)] / 6  (I remembered there was a formula and its easy to proof by induction but I ended up googling the formula first before I could prove it)

## performance
#  Have to go to real large numbers to see a difference
## n -      formula      iterate    
## 10ˆ6     0.000        0.6          
## 10ˆ6     0.000        6.747     


import sys

def calculate_iterate(top_number):
	s1 = (sum(i for i in range(1, top_number + 1)) ) ** 2
	s2 = sum(i**2 for i in range(1, top_number + 1))
	return int(s1 - s2)

def calculate_formula(top_number):
	s1 = (top_number * (top_number + 1) / 2 ) ** 2
	s2 = (top_number * (top_number + 1) * (2* top_number + 1) / 6 )
	return int(s1 - s2)


if __name__ == "__main__":
    # usage..  006.py high_limit method{'formula' | 'iterate' }

    try:
        input_value = int(sys.argv[1])
        method_to_use = sys.argv[2]
    except IndexError:
        input_value = 100      # run with default input 1000 
        method_to_use = 'formula'  # and use default easy method if none provided


    if method_to_use == 'formula':
        print(calculate_formula(input_value))

    if method_to_use == 'iterate':
        print(calculate_iterate(input_value))    