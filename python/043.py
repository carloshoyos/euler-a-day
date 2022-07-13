"""
Project Euler Problem 43
========================

The number, 1406357289, is a 0 to 9 pandigital number because it is made
up of each of the digits 0 to 9 in some order, but it also has a rather
interesting sub-string divisibility property.

Let d[1] be the 1st digit, d[2] be the 2nd digit, and so on. In this
way, we note the following:

  * d[2]d[3]d[4]=406 is divisible by 2
  * d[3]d[4]d[5]=063 is divisible by 3
  * d[4]d[5]d[6]=635 is divisible by 5
  * d[5]d[6]d[7]=357 is divisible by 7
  * d[6]d[7]d[8]=572 is divisible by 11
  * d[7]d[8]d[9]=728 is divisible by 13
  * d[8]d[9]d[10]=289 is divisible by 17

Find the sum of all 0 to 9 pandigital numbers with this property.
"""

# brute force is fairly fast, reusing problem 41 (all pandigital numbers using permutations), and checking against a list of primes. 
# this taakes 4.05 seconds to run.  There are faster ways using fact that position 6 has to be 0 or 5, and position 2 has to be even, and 8-10 are divisible by 17 and unique digits (39 possible options)

import itertools


def isSubdivisible(num):
  num = str(num)
  primes = [2,3,5,7,11,13,17]
  for i in range(0,7):
    if int(num[1+i:4+i:])%primes[i]:
      return False
  return True


## the non pythonic way to do this 
# sum = 0 
# for n in itertools.permutations("1234567890",10): 
#   if isSubdivisible(int("".join(n))):
#     #print( int("".join(n)) ) 
#     sum += int("".join(n))



# same as above, but pythonic 
print(sum([int("".join(x)) for x in itertools.permutations("1234567890",10) if isSubdivisible(int("".join(x)))]))