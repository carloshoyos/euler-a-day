"""
Project Euler Problem 40
========================

An irrational decimal fraction is created by concatenating the positive
integers:

                  0.123456789101112131415161718192021...
                               ^

It can be seen that the 12th digit of the fractional part is 1.

If d[n] represents the n-th digit of the fractional part, find the value
of the following expression.

    d[1] * d[10] * d[100] * d[1000] * d[10000] * d[100000] * d[1000000]
"""

# wow..  nice of pythont that we can calculate the concatenations of the first 1 million numbers and just multiply the digits in specific positions.

s = "".join(str(i) for i in range(1,1000000))

result = 1
position = 1

while position < 1000001:
    result *= int(s[position-1])
    #print(position, result)
    position *= 10

print(result)