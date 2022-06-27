"""
Project Euler Problem 28
========================

Starting with the number 1 and moving to the right in a clockwise
direction a 5 by 5 spiral is formed as follows:

                              21 22 23 24 25
                              20  7  8  9 10
                              19  6  1  2 11
                              18  5  4  3 12
                              17 16 15 14 13

It can be verified that the sum of both diagonals is 101.

What is the sum of both diagonals in a 1001 by 1001 spiral formed in the
same way?
"""

# two approaches:  
#  1- brute force, calculate the spiral in a 2d array. 
#  2- look for a pattern.  You can calculate the sum of the outer ring once you see the top right corner is  nˆ2.

size = 1001 

def getNextDirection():
    while True:
        yield (1, 0)
        yield (0, 1)
        yield (-1,0)
        yield (0,-1)

# using a 2d list, but these can be tricky in python.  A better alternative is to use 2d arrays in numpy. 
def calculate_by_generating(size):
    spiral = [[0]*size for i in range(size)]    # initializing a 2d array list of lists 

    x = y  = size//2 
    spiral[y][x] = n = 1  # first number, n iterates

    dir = getNextDirection()

    for i in range(1, size):
        for j in range(0,2): # number of elements to add increases every 2 iterations
            dx, dy  = next(dir)
            for k in range(1, i+1):
                x,y,n = x+dx, y+dy, n+1
                spiral[y][x] = n

    # formula above has not calculated the last (top) row.  But we know top corner is n^2, so easier to just add it at the end
    return sum([spiral[x][y] if (x == y or x+y == size-1) else 0 for x in range(0, size) for y in range(0, size)]) + size ** 2



# The top right corrner is n^2  (proof by induction, to go from n to n+1  you add 4 times n+1 (for each of the sides). So the n+1 corner is n^2 + 4*(n+1) == (n+1)^2 )
# going clock wise, the previos corners are:  n^2-n+1,  n^2-2n+2 and n^2-3n+3   
# adding all up, you get 4n^2 -6n + 6 

def calculate_by_formula(size):
    ans = 1  # Special case for size 1
    ans += sum(4 * n ** 2  - 6*n + 6 for n in range(3, size + 1, 2))
    return str(ans)

print(calculate_by_formula(size))
#print(calculate_by_generating(size))