"""
Project Euler Problem 16
========================

2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2^1000?
"""


# oh wow...  one amazing thing about python is that int has auto precision (int is the new long), so things like 2^1000 are auto adjusted

result = 2**1000

digit_sum = 0
for i in str(result):
    digit_sum += int(i)

print(digit_sum)