"""
Project Euler Problem 30
========================

Surprisingly there are only three numbers that can be written as the sum
of fourth powers of their digits:

  1634 = 1^4 + 6^4 + 3^4 + 4^4
  8208 = 8^4 + 2^4 + 0^4 + 8^4
  9474 = 9^4 + 4^4 + 7^4 + 4^4

As 1 = 1^4 is not a sum it is not included.

The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be written as the sum of fifth
powers of their digits.
"""

# first approach, brute force, evaluate all numbers below an estimated ceiling. 

# To estimate a ceiling notice that  9^5  ~= 59k 
# so the numbers will have 6 digits or less as for a 7 digit number, the max sum is < 7 * 60K = 480k which has 6 digits. 
# also, the maximum will be < 60k * 6 = 360k 



def get_fifth_power_of_digits(number):
  return sum([int(x)** 5 for x in str(number)])


# option 1 - c style iteration
# stumbled at first because I was including 1 (which the question explicitly explains is not a valid solution). 
s = 0 
for i in range(2, 360000): # start at 2 b/c 1 won't be a sum
  if get_fifth_power_of_digits(i) == i:
    s += i
print(s)

# option 2 - a more compressed way to write this and runs a tiny bit faster
print(sum([i for i in range(2, 360000) if i == get_fifth_power_of_digits(i)]))
