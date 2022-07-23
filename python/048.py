"""
Project Euler Problem 48
========================

The series, 1^1 + 2^2 + 3^3 + ... + 10^10 = 10405071317.

Find the last ten digits of the series, 1^1 + 2^2 + 3^3 + ... + 1000^1000.
"""


# two appraoches.  
# First, brute force: # python auto types means we can just calculate this beast of a number
# Second, using modulus distributive property, we can simply iterrate and calculate the first 10 digits 
#  a^b mod n 
#   = a^(b-1) * a  mod n 
#   = a^(b-1) * a  mod n 
#   = a^(b-1) mod n  *   a mod n 
#   etc..  



# approach 1 - brute force 
print(sum([n**n for n in range (1,1000)]) % 10**10 )

# approach 2 - only calculate first 10 digits 

s = 0
for d in range(1,1001):
    n = 1
    for i in range(1,d+1):
        n = n * d % 10**10
    s += n

print(s % 10**10)