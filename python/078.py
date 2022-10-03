"""
Project Euler Problem 78
========================

Let p(n) represent the number of different ways in which n coins can be
separated into piles. For example, five coins can separated into piles in
exactly seven different ways, so p(5)=7.

                            OOOOO

                            OOOO   O

                            OOO   OO

                            OOO   O   O

                            OO   OO   O

                            OO   O   O   O

                            O   O   O   O   O

Find the least value of n for which p(n) is divisible by one million.
"""

# two appraoches.  
# #1 - first one (naive), use problem 76 to generate all possible sums to n (since a sum is the same as a partition)
#   suspect it will take too long to run 
# #2 - use a generating function.  Spend 30 mins to see if I can figure it out, but ended up googling it, and of course it was another euler finding.
#       https://en.wikipedia.org/wiki/Pentagonal_number_theorem 
#       55374  


import functools
import time

# approach # 1
# note that we add +1 to the result because the partition of "all objects"
# this works for the first 2000 numbers before becoming too slow and the solution was not in the first 2000
# note that 

def countSubPartitions(upper_limit):
    numbers = range(1, upper_limit)
    ways = [1] + [0] * upper_limit

    for i in numbers:
        for j in range(i, upper_limit+1):
            ways[j] += ways[j - i]
        #print(i, ways)
    return(ways[upper_limit]+1)


# approach # 1b, 
# same as 1, but only add numbers mod 1000000 since we only care about the first 6 digits.  
# this should reduce the memory consumption and time to run.  This took 5 minutes to run and find the answer.    

def countSubPartitionsModM(upper_limit, m, target):

    t = time.time()
    numbers = range(1, upper_limit)
    ways = [1] + [0] * upper_limit
    for i in numbers:

        ## uncomment this to print progress
        # if i%2500 == 0:
        #     print(i, time.time()-t)
        #     t = time.time()

        for j in range(i, upper_limit+1):
            ways[j] += ways[j - i]
            ways[j] = ways[j] % m
            # if ways[j] == 0:
            #     print(f"found {j}")s
        
        if ways[i]== target:
            print(f"found {i}", ways[i])
    return(ways[upper_limit]+1)


# approach # 2
# a generating function (thanks Euler!) using pentagonal numbers 
# note that this will only work if you start from 1 and evaluate incrementally so that the caching prevents maximum recusion length errors
# jeezz...  what did Euler not do? 

@functools.cache
def SubPartitionsPengtagonalGen(n):
    if n<0: return 0
    if n<2: return 1
    sm=0
    for k in range(1, n+1):
        n1 = n-k*(3*k-1)//2
        n2 = n-k*(3*k+1)//2
        sm += (-1)**(k+1) * (SubPartitionsPengtagonalGen(n1) + SubPartitionsPengtagonalGen(n2))
        if n1 <= 0:
            break
    return sm%1000000


# uncomment this to run approach 1
countSubPartitionsModM(60000, 1000000, 0)


# uncomment this to run approach 2
n = 1
while SubPartitionsPengtagonalGen(n)!=0.0: n += 1
print(n)


