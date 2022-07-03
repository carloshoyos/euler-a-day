"""
Project Euler Problem 34
========================

145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of
their digits.

Note: as 1! = 1 and 2! = 2 are not sums they are not included.
"""

# this is an easy calculation once we find a ceiling for the problem.  9! is aprox 362k (6 digits).  
# so number will be below 7 digits, and under 7 * 9! = 2540160

fact = [1,1,2,6,24,120,720,5040,40320,362880]  # too lazy?? yes, this can be calculated

total = 0
for i in range (3, 2540160):
    if sum([fact[int(x)] for x in str(i)]) == i:
        total += i
        #print(i)
print(total)