"""
Project Euler Problem 74
========================

The number 145 is well known for the property that the sum of the
factorial of its digits is equal to 145:

1! + 4! + 5! = 1 + 24 + 120 = 145

Perhaps less well known is 169, in that it produces the longest chain of
numbers that link back to 169; it turns out that there are only three such
loops that exist:

169 363601 1454 169
871 45361 871
872 45362 872

It is not difficult to prove that EVERY starting number will eventually
get stuck in a loop. For example,

69 363600 1454 169 363601 ( 1454)
78 45360 871 45361 ( 871)
540 145 ( 145)

Starting with 69 produces a chain of five non-repeating terms, but the
longest non-repeating chain with a starting number below one million is
sixty terms.

How many chains, with a starting number below one million, contain exactly
sixty non-repeating terms?
"""

# approach a) brute force try every chain 
# approach b) two dictionaries, one to cache the factorials and one to cache each number chain. If we have already seen a number (chain value has been calculated), then we use the cached value. 
# approach b is 10 times faster than approach a (51 seconds vs 4.3 seconds)



import math
import time


upper_limit = 1000000

## approach a, brute force 

start = time.time()

total = 0
for i in range(1,upper_limit):
    digit = str(i)
    chain = {digit}
    while True:
        digit = str(sum([math.factorial(int(d)) for d in digit]))
        if digit in chain:
            break
        chain.add(digit)

    if len(chain) == 60:
        total +=1 

print(total)
print(time.time() - start)

# approach b, cache results

start = time.time()
total = 0
factorials = {d:math.factorial(d) for d in range(0,10)}



chain_count = {}
for i in range(1,upper_limit):
    length = 1
    digit = str(i)
    chain = {digit}
    while True:
        digit = str(sum([math.factorial(int(d)) for d in digit]))

        # add to cache        
        if digit in chain_count:
            length = len(chain) + chain_count[digit]
            break

        if digit in chain:
            length = len(chain)
            break
        chain.add(digit)

    chain_count[str(i)] = length
    if length == 60:
        total +=1 

print(total)
print(time.time() - start)