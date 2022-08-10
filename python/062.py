"""
Project Euler Problem 62
========================

The cube, 41063625 (345^3), can be permuted to produce two other cubes:
56623104 (384^3) and 66430125 (405^3). In fact, 41063625 is the smallest
cube which has exactly three permutations of its digits which are also
cube.

Find the smallest cube for which exactly five permutations of its digits
are cube.
"""

# two approaches...  
# 1- generate cubes ascending.. and for each cube look at all the permutations of its digits and see if its also a cube.  End when first count is 5. 
# this was really slow, made me think of a diferent approach: 

# 2- generate cubes, and for each sort its digits and keep count in a dictionary of # of cubes with those digits (by increasign +1)
# if the count hits 5, then you have a winner. 


import itertools as it

permutations = 5

# approach 1 test each cube and see how many of its permutations are cubes , this has terrible performance
def calculate_test_all_combs():
    max_space = 10000 # number of cubes to explore
    cubes = set([x**3 for x in range(1, max_space)])

    for x in sorted(cubes):
        if x > 10000000000: 
            break
        
        # get all unique permutations of the digits of x (set used to get unique)
        perm = set([int(''.join(perm)) for perm in it.permutations(str(x), len(str(x)))])

        # count how many are cubes (assumes the cubes list has all cubes of length x)
        perm_cube_count = sum([1 if x in cubes else 0 for x in perm])
        if perm_cube_count > 2:
            print(x, perm_cube_count)
#calculate_test_all_combs()



# approach 2 
# keep a dictionary where the key is the sorted digits of the cube, and the valueu is the list of cubes that can be generated with those digits
# start filling that dictionary incrementally by increasing each cube until the updated list has 5 elements 

def calculate_test_all_increments():

    cube_count = dict() 

    for n in it.count(1):
        n_cubed = n**3
        digits = "".join(sorted(str(n_cubed)))

        cubes = cube_count.get(digits, [])
        if len(cubes) == permutations-1:
            #print(n, n_cubed, cubes)
            print(min(cubes))
            break

        cube_count[digits] = cubes + [n_cubed]

calculate_test_all_increments()
