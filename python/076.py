"""
Project Euler Problem 76
========================

It is possible to write five as a sum in exactly six different ways:

4 + 1
3 + 2
3 + 1 + 1
2 + 2 + 1
2 + 1 + 1 + 1
1 + 1 + 1 + 1 + 1

How many different ways can one hundred be written as a sum of at least
two positive integers?
"""


# started by reusing problem 31, but approach (a) (brute force takes forever), and approach (b) still took +8mins 
# option 1: recursive (which is expensive as it will calculate all permutations of all coins until sum is above target value).  
# option 2: dynamic programing. This article does a much better job at explaining.   https://www.geeksforgeeks.org/coin-change-dp-7/ 
# option 3: ...  some research here.  Euler came up with partition functions!!  https://mathworld.wolfram.com/PartitionFunctionP.html
#           note that for the result is + 1 as the partition function include the no sum option (5 = 5) and the solution asks only for the groups where there is at least one sum (e.g. 5 = 4+1) 
# option 4: this shoudl have been the default dynamic programing approach.  

import  time

upper_limit = 100
coins = range(1,upper_limit)   # this has coins up to upper_limit-1  since range is [)
allSets = set()

# approach 1: recursive calculate all valid combinations in allSets

# for each coin c, call function again trying to make sum s-c with the same coins. 
# Keep a list of coins used as the function is called. 
# If you hit sum == 0, you got a valid collection. 
# keep a set of all valid collections to avoid counting doubles. 
def getAllCoinChangesRecursive(coins, coin, sum, changeSet):
  global allSets
  subset = []
  #print("iterating on", coin, sum, changeSet)
  if sum == 0:
    allSets.add(tuple(sorted(changeSet)))
    return 
  elif sum < 0:
    return 

  for c in coins:
    if c <= sum:
      sets = getAllCoinChangesRecursive(coins, c, sum-c, changeSet+[c])
  return


# approach 2: dynamic approach.  This generates all the combinations (in global variable allSets), and also counts them. 
# for every step split problem in two:  (i)  getting to the sum with all but the last coin, and (ii) using the last coin c, and getting to the sum s-c. 
# repeat recursively.  
def getAllCoinChangesDynamic(S, m, n, changeSet ):
    global allSets
 
    # If n is 0 then we have found a solution, add it to the there is 1 solution (do not include any coin)
    if (n == 0):
        allSets.add(tuple(sorted(changeSet)))
        return 1
 
    # If n is less than 0 then the last coin added is above the total, can be ignored  
    if (n < 0):
        return 0
 
    # After adding all the selected coins, the sum doesn't reach the total -> can be ignore
    if (m <=0 and n >= 1):
        return 0
 
    # count is sum of two solutions (i) + (ii):
    #   (i) excluding the last coin (try with the reminding coins) 
    #  (ii) using the last coin see if you can reach total-last coin. 
    return getAllCoinChangesDynamic( S, m - 1, n, changeSet ) + getAllCoinChangesDynamic( S, m, n-S[m-1],  changeSet+ [S[m-1]]);

# approach 3: euler generating function
# need to store already calculated values in a cache, but with functools cache, we can ignore that
# 
import functools

@functools.cache 
def getAllPartitionCount(n):
    if n<0: return 0 # P(n) = 0 for n < 0
    if n == 1: return 1
    value = 0
    for i in range(1, n+1):
        p1 = getAllPartitionCount(n - i * (3 * i - 1) // 2)
        p2 = getAllPartitionCount(n - i * (3 * i + 1) // 2)
        if(i % 2 == 1):
            value = value + p1 + p2
        else:
            value = value -  (p1 + p2)

    return value



# approach 1
# allSets = set()
# getAllCoinChangesRecursive(coins,len(coins),upper_limit, [])
# print(len(allSets))

##approach 2
# st = time.time()
# allSets = set()
# getAllCoinChangesDynamic(coins,len(coins),upper_limit, [])
# print(len(allSets))
# print("time", time.time()-st)


# #approach 3, euler generting function
# print(getAllPartitionCount(upper_limit+1)-1)

## approach 4
## what an easy approach - this is a better dynamic programing approach.  
## start with assumption that each number n can be written in one way "n" 
## then iterate, for each number k, add the ways that the number n-k can be added  (this is calculating n-k ways + k )


def countSubPartitions(upper_limit):
    numbers = range(1, upper_limit)
    ways = [1] + [0] * upper_limit

    for i in numbers:
        for j in range(i, upper_limit+1):
            ways[j] += ways[j - i]
        print(i, ways)
    return(ways[upper_limit])

countSubPartitions(15)