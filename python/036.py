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
# a way to speed this up is to not test all numbers for palindromic, but to start by generating all palindromic numbers (concat abc + cba )

def isPalindromic(num):
    return str(num) == str(num)[::-1]

def getMultiBasePalindromic_all(max):
    return ( sum( [i for i in range(1, max) if isPalindromic(i) and isPalindromic(str(bin(i))[2:]) ]))

# the non pythonic way to do this
# total = 0
# for i in range(1, 1000000):    # no trailing zeros 
#     if isPalindromic(i) and isPalindromic(str(bin(i))[2:]):
#         print(i, bin(i))
#         total += i
# print(total, "\n\n")



# the faster way to do this by generating the palindromic numbers by merging abc + cba (for even length), and abc + m + cba (for odd length) numbers
# TODO: max length is hardcoded, make it a parameter

def getMultiBasePalindromic_gen():
    total = 0

    tens = [str(x) for x in range(1, 100)] 
    hun = [str(x) for x in range(100, 1000)] 

    for i in tens + hun:    # even digits 
        j = int(str(i) +  str(i)[::-1])
        if isPalindromic(str(bin(j))[2:]):
            total += j

    for i in tens + ['']:    # odd digits 
        for m in range(0,10):
            j = int(str(i) +  str(m) + str(i)[::-1])
            if isPalindromic(str(bin(j))[2:]):
                total += j

    return total



print(getMultiBasePalindromic_gen())
print(getMultiBasePalindromic_all(1000000))
