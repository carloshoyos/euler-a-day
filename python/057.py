"""
Project Euler Problem 57
========================

It is possible to show that the square root of two can be expressed as an
infinite continued fraction.

            2 = 1 + 1/(2 + 1/(2 + 1/(2 + ... ))) = 1.414213...

By expanding this for the first four iterations, we get:

1 + 1/2 = 3/2 = 1.5
1 + 1/(2 + 1/2) = 7/5 = 1.4
1 + 1/(2 + 1/(2 + 1/2)) = 17/12 = 1.41666...
1 + 1/(2 + 1/(2 + 1/(2 + 1/2))) = 41/29 = 1.41379...

The next three expansions are 99/70, 239/169, and 577/408, but the eighth
expansion, 1393/985, is the first example where the number of digits in
the numerator exceeds the number of digits in the denominator.

In the first one-thousand expansions, how many fractions contain a
numerator with more digits than denominator?
"""

# After working a few iterations on paper, there's a formula to calculate numerator and denominator: 
# start with: 


# f(n+1) = 1 + 1 / (2 + f(n)) 
# 
# lets try to find a function for numerator and denominator, i.e. 
#   f(n) = num(n) / den(n)
#   f(n+1) = num(n+1)/num(n+1) = 1 + 1 / (2 + num(n)/den(n))
# . // done on paper, being lazy to transcribe here ... 
# . 
# . 
#   f(n+1) = num(n+1)/num(n+1) ==  (2*den(n) + num(n)) /  ( den(n) + num(n) )`
#
# 
# Using these formulas solution is straight forward
# num(n+1) = 2*den(n) + num(n)
# den(n+1) =  den(n) + num(n)


# could simplify further by not storing all values in a list, just previous one and counting in the loop
length = 1000

a = [0]*length
b = [0]*length

a[0] = 1
b[0] = 1

for n in range(1,length):
    a[n] = 2*b[n-1] + a[n-1]
    b[n] = b[n-1] + a[n-1]
    n +=1

print(  sum([1 if (len(str(a[n])) > len(str(b[n])) ) else 0 for n in range(0,length) ])) 