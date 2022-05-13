"""
Project Euler Problem 1
=======================

If we list all the natural numbers below 10 that are multiples of 3 or 5,
we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""
# fairly simple starter problem. I try two approaches here: 
# a) iterate through all numbers and sum those that match the divisibility condition (num %3 or num %5 == 0)
# b) use triangular number equation, i.e. triangleSum(n) = n(n+1)/2 =  1+2+...+n, adding all 3 and 5 numbers ( e.g. 3 * triangleSum(upper-1)  ) minus the numbers divisible by 15 (as they will be counted twice)

## gotchas 
# since the problem asks for numbers below n, the top number has to be decremented by one for the triangle sum to match.    

## performance
#  for approach (a) (iteration), there are two functions. a1 (easySum) is the typical c style of loop and if, while a2 (pythonicSum) is all in one line 
#  performance calculated using `python -m cProfile 001.py` 

## n -      easySum     pythonicSum     gaussTrickSum
## 10^6     0.109       0.169           0.000
## 10^7     1.011       1.693           0.000
## 10^8     10.06       16.01           0.000
## 10^9     103.75      164.79          0.000

import sys



# a1) trivial brute force approach, simply iterate on a loop, c style
def easySum(upper_limit):
    answer = 0
    for i in range(1,upper_limit):
        if (i%3 == 0) or (i%5 == 0): 
            answer = answer + i 
    print(answer)


# a2) a more pythonic compressed style, all code in one line.  will be used to compare benchmarks
def pythonicSum(upper_limit):
    answer = sum(i for i in range(1, upper_limit) if ((i%3 == 0) or (i%5 == 0)) )
    print(answer)

# b) This is inspired by the story that a primary school Gauss was given a challenge (punished ?) to sum the numbers 1 to 100 by his teacher. 
# by pairing first and last he was able to deduct the triangular sum formula triangleSum(n) = n(n+1)/2 =  1+2+...+n,

def triangleSum(n):

    return int(n*(n+1)/2)

def gaussTrickSum(upper_limit):
    threeSum = 3 * triangleSum((upper_limit-1)//3)
    fiveSum = 5 * triangleSum((upper_limit-1)//5)
    fifteenSum = 15 * triangleSum((upper_limit-1)//15)

    print( threeSum + fiveSum - fifteenSum)

#gaussTrickSum(100000)

if __name__ == "__main__":

    # usage..  p001.py upper_bound method {'easy' | 'pythonic' | 'gauss'}

    try:
        input_value = int(sys.argv[1])
        method_to_use = sys.argv[2]
    except IndexError:
        input_value = 1000      # run with default input 1000 
        method_to_use = 'easy'  # and use default easy method if none provided


    if method_to_use == 'easy':
        easySum(input_value)
    elif method_to_use == 'pythonic':
        pythonicSum(input_value)
    else:
        gaussTrickSum(input_value)

