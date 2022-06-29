"""
Project Euler Problem 31
========================

In England the currency is made up of pound, -L-, and pence, p, and there
are eight coins in general circulation:

  1p, 2p, 5p, 10p, 20p, 50p, -L-1 (100p) and -L-2 (200p).

It is possible to make -L-2 in the following way:

  1 * -L-1 + 1 * 50p + 2 * 20p + 1 * 5p + 1 * 2p + 3 * 1p

How many different ways can -L-2 be made using any number of coins?
"""


# More complex implementation, we calculate all the solution sets and then count then to return different ways to make change. 

# two approaches: 
# option 1: recursive (which is expensive as it will calculate all permutations of all coins until sum is above target value).  
# option 2: dynamic programing. This article does a much better job at explaining.   https://www.geeksforgeeks.org/coin-change-dp-7/ 


coins = [1, 2, 5,10,20, 50, 100, 200] #1, 2, 5, 10, 
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

# approach 1
# allSets = set()
# getAllCoinChangesRecursive(coins,len(coins),200, [])
# print(len(allSets))

allSets = set()
getAllCoinChangesDynamic(coins,len(coins),200, [])
print(len(allSets))