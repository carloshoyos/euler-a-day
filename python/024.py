"""
Project Euler Problem 24
========================

A permutation is an ordered arrangement of objects. For example, 3124 is
one possible permutation of the digits 1, 2, 3 and 4. If all of the
permutations are listed numerically or alphabetically, we call it
lexicographic order. The lexicographic permutations of 0, 1 and 2 are:

                    012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits 0, 1, 2, 3,
4, 5, 6, 7, 8 and 9?
"""

# Two approaches.  
# a) brute force, 
# b) knowing there are 10! possible permutations, we can calculate the first
#    digit 1000000 // (10! / 10) (as there are 9! combinations starting with each of the 10 digits)
#    then continue with the reminder for the second digit etc..  


# performance.  itertools is very fast so we won't see a difference unless going to much higher numbers.
# the numberr of digits doesn't affect as much as the position.  The higher the position the longer it will take iterate.   

#  1  million digit
## digits -     iterate      formula      
## 10           0.017        0.002
## 100          0.016        0.002             1 million digit
## 1000         0.15        0.002             1 million digit
## 1000         1.502        0.001             10 million digit

import itertools
import math
import sys


# approach 1 - brute force using itertools.permutations to calculate all the permutations 
def nthpermutation(digits, position):
    temp = itertools.islice(itertools.permutations(digits), position-1, None)
    i = next(temp)
    return("".join(str(x) for x in i))


# approach 2 - calculate the nth digit by seeing in which group of the remaining (total_digits - n + 1) subset the target position is
#  if the reminder is zero, note that the list of digits remining is indexed at 0, but the divisions start at 1, so 

def nthpermutation_formula(digits, position):
    answer = ""
    for i in range(10,0,-1):
        div, rem = divmod(position, math.factorial(i-1) )

    # ajust for edge case.. when reminder is zero, it will be the last permutation of the previous group, so substract one to the division.
        if rem == 0: 
            div -=1
        answer += str(digits[div])
        del digits[div]
    #print('cycle (i/tot/fact): (', i, ceiling, math.factorial(i-1), ') in group: ', div, '  - with rem: ', rem, digits, answer)
        position = rem 
    return(answer)




if __name__ == "__main__":
    # usage..  024.py digits method{'formula' | 'iterate' }
    digit_size = 10
    digits = list(range(0,digit_size))
    position = 1000000  # default 1 million position 
    try:
        digit_size = int(sys.argv[1])
        method_to_use = sys.argv[2]
    except IndexError:
        digit_size = 10     # run with default 10 digits 
        method_to_use = 'iterate'  # and use default easy method if none provided

    sum = 0 
    if method_to_use == 'iterate':
        digits = list(range(0,digit_size))
        print(nthpermutation(digits, position))


    if method_to_use == 'formula':
        digits = list(range(0,digit_size))
        print(nthpermutation_formula(digits, position))

