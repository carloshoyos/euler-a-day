"""
Project Euler Problem 67
========================

By starting at the top of the triangle below and moving to adjacent
numbers on the row below, the maximum total from top to bottom is 23.

                                    3
                                   7 4
                                  2 4 6
                                 8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom in triangle.txt, a 15K text file
containing a triangle with one-hundred rows.

NOTE: This is a much more difficult version of Problem 18. It is not
possible to try every route to solve this problem, as there are 2^99
altogether! If you could check one trillion (10^12) routes every second it
would take over twenty billion years to check them all. There is an
efficient algorithm to solve it. ;o)
"""

data = """75
                                  95 64
                                 17 47 82
                               18 35 87 10
                              20 04 82 47 65
                            19 01 23 75 03 34
                           88 02 77 73 07 63 67
                         99 65 04 28 06 16 70 92
                        41 41 26 56 83 40 80 70 33
                      41 48 72 33 47 32 37 16 94 29
                     53 71 44 65 25 43 91 52 97 51 14
                   70 11 33 28 77 73 17 78 39 68 17 57
                  91 71 52 38 17 14 91 43 58 50 27 29 48
                63 66 04 68 89 53 67 30 73 16 69 87 40 31
               04 62 98 27 23 09 70 98 73 93 38 53 60 04 23"""

# the tip makes this problem real straightforward..  
# just start at the bottom and calculate up a row the max of the two sums until you get to the top. 

# note that the text file had a trailing new line that would throw things off.  
# 


with open('resources/triangle.txt', 'r') as f: 
    data = f.read()

triangle = [x.split() for x in data.split("\n")]
size = len(triangle)

# for each row from bottom to top, calculate the max sum of either left or right node. 
# new node will have the max partial sum up to that point.  
# continue until you get to the top. 
for i in range(size-2,-1,-1):
    for j in range(0, i+1):
        triangle[i][j] = max(int(triangle[i+1][j]), int(triangle[i+1][j+1])) + int(triangle[i][j])


print(triangle[0][0])
