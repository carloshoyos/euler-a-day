"""
Project Euler Problem 39
========================

If p is the perimeter of a right angle triangle with integral length
sides, {a,b,c}, there are exactly three solutions for p = 120.

                    {20,48,52}, {24,45,51}, {30,40,50}

For which value of p < 1000, is the number of solutions maximised?
"""

# two ways to solve: 
# a) brute force, i.e. find all partitions where a+b+c = x and a^2 + b^2 = c^2. This took long.
# b) only evaluat for P to be even:   
#     - if both a and b are either even or odd,  a^2 + b^2 is even so c is even and perimeter is even )   
#     - if  a and b are odd / even, a^2 + b^2 is odd -> perimeter is odd + even + odd = even


def countSolutionsTriangle(perimeter):
    solutions = 0 
    for a in range(1,perimeter // 2):
        for b in range(a,perimeter-a):
            c = perimeter - a - b
            if a ** 2 + b ** 2 == c ** 2:
                solutions += 1
    return solutions


max_solution = 0
max_perim = 0

for i in range(2,1001, 2): # only even numbers
    s = countSolutionsTriangle(i)
    if s > max_solution:
        max_solution = s
        max_perim = i 

print(max_perim)

# more pythonic way to solve this
# print(max(range(2, 1001, 2), key=countSolutionsTriangle))