"""
Project Euler Problem 26
========================

A unit fraction contains 1 in the numerator. The decimal representation of
the unit fractions with denominators 2 to 10 are given:

   1/2  =  0.5
   1/3  =  0.(3)
   1/4  =  0.25
   1/5  =  0.2
   1/6  =  0.1(6)
   1/7  =  0.(142857)
   1/8  =  0.125
   1/9  =  0.(1)
  1/10  =  0.1

Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can
be seen that ^1/[7] has a 6-digit recurring cycle.

Find the value of d < 1000 for which ^1/[d] contains the longest recurring
cycle in its decimal fraction part.
"""

# For each number iterate dividing the reminder * 10 until a cycle is detected, or the reminder is zero. 
# This can be further simplified by combining the checks for period and division complete. 

longest_period = 0
longest_number = 1

for i in range(2,1000):
  reminders = [0]
  rem = 1
  period = 0
  while rem != 0 and rem not in reminders:
    reminders.append(rem) 
    rem = (rem * 10) % i
  if(rem != 0):
    period = len(reminders) - reminders.index(rem)
    if period > longest_period:
      longest_number = i
      longest_period = period

print(longest_number)