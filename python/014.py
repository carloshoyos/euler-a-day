"""
Project Euler Problem 14
========================

The following iterative sequence is defined for the set of positive
integers:

n->n/2 (n is even)
n->3n+1 (n is odd)

Using the rule above and starting with 13, we generate the following
sequence:
                  13->40->20->10->5->16->8->4->2->1

It can be seen that this sequence (starting at 13 and finishing at 1)
contains 10 terms. Although it has not been proved yet (Collatz Problem),
it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
"""

#two approaches. One naive, brute force calculate for each nmber. 
# the second one, cache numbers that have already been calculated, and check against cache before calculating

## performance
#  Have to go to real large numbers to see a difference
## n -      brute      cache    
## 10ˆ6     3.828      2.18s          
## 10^7


def collatz_length_naive(x, len):
    if x == 1:
        return len
    if x % 2 == 0: 
        return 1+collatz_length_naive(x//2, len)
    if x %2 == 1:
        return 1+collatz_length_naive(3*x+1, len)



coll_leng = {}
#print(coll_leng)
def collatz_length_cache(x, len):
    global coll_leng
    if coll_leng.get(x,0): 
        return coll_leng[x]
    if x == 1:
        return len
    if x % 2 == 0: 
        return 1+collatz_length_cache(x//2, len)
    if x %2 == 1:
        return 1+collatz_length_cache(3*x+1, len)

collatz_length_cache(13, 1)

longest = 1 
longest_number = 1 
i = 2

while i < 1000000:
    test_length = collatz_length_cache(i, 1)
    coll_leng[i] = test_length
    if test_length > longest:
        longest_number = i
        longest = test_length
    i += 1
print(longest_number)