"""
Project Euler Problem 52
========================

It can be seen that the number, 125874, and its double, 251748, contain
exactly the same digits, but in a different order.

Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x,
contain the same digits.
"""

# back to a fairly easy problem.  Brute force and using set to calculate the unique digits of a number. 
# it's unclear if the problem allows for repeated digits, but the solution worked with set. 


max_products = 6 # 6x 


def getMinProductHasSameDigits(max_products = 2):
    n = 10
    while True:
        n += 1
        digits = set(str(n))
        for i in range(2, max_products+1):
            if set(str(i * n)) != digits:
                break
            elif i == max_products:
                #print("found solution {} for {} multiplications {}".format(n, max_products, [n*i for i in range(1, max_products+1)]))
                return n


print(getMinProductHasSameDigits(max_products))