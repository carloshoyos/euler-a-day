"""
Project Euler Problem 36
========================

The decimal number, 585 = 1001001001[2] (binary), is palindromic in both
bases.

Find the sum of all numbers, less than one million, which are palindromic
in base 10 and base 2.

(Please note that the palindromic number, in either base, may not include
leading zeros.)
"""

# computers are fast..  just a little bit of glue and int <-> string conversion and bin function to convert base. 

def isPalindromic(num):
    return str(num) == str(num)[::-1]


print( sum( [i for i in range(1,1000000) if isPalindromic(i) and isPalindromic(str(bin(i))[2:]) ]))


# the non pythonic way to do this
# for i in range(1, 1000000):    # no trailing zeros 
#     if isPalindromic(i) and isPalindromic(str(bin(i))[2:]):
#         print(i, bin(i))



