"""
Project Euler Problem 68
========================

Consider the following "magic" 3-gon ring, filled with the numbers 1 to 6,
and each line adding to nine.

Working clockwise, and starting from the group of three with the
numerically lowest external node (4,3,2 in this example), each solution
can be described uniquely. For example, the above solution can be
described by the set: 4,3,2; 6,2,1; 5,1,3.

It is possible to complete the ring with four different totals: 9, 10, 11,
and 12. There are eight solutions in total.

        Total          Solution Set
        9              4,2,3; 5,3,1; 6,1,2
        9              4,3,2; 6,2,1; 5,1,3
        10             2,3,5; 4,5,1; 6,1,3
        10             2,5,3; 6,3,1; 4,1,5
        11             1,4,6; 3,6,2; 5,2,4
        11             1,6,4; 5,4,2; 3,2,6
        12             1,5,6; 2,6,4; 3,4,5
        12             1,6,5; 3,5,4; 2,4,6

By concatenating each group it is possible to form 9-digit strings; the
maximum string for a 3-gon ring is 432621513.

Using the numbers 1 to 10, and depending on arrangements, it is possible
to form 16- and 17-digit strings. What is the maximum 16-digit string for
a "magic" 5-gon ring?
"""

# lets create a data structure to represent a 5-gon ring. 
# First, label the nodes clockwise starting at zero from outside to inside, 
#        0
#         \
#   4--5---6   1
#     /     \ /
#    9       7
#   / \     /
#  3   \   /
#       \ /
#        8
#         \
#          2

# then the lines are in positions (0,6,7), (1,7,8), etc... as defined in list linepos 

linepos = [[0,6,7], [1,7,8], [2,8,9],[3,9,5],[4,5,6]]

# create and analyse all permutations using itertools 

import itertools
rings = list(itertools.permutations(range(1,11)))

maxring = 0

# test each possible ring
for ring in rings:

        string = ""
        # check that the minimum line is the top one (position 0)
        if ring[0] == min(ring[0:5]): 

                # check that the sum of all lines is the same (a set of all line sums should have length 1)
                if len(set([ring[line[0]] + ring[line[1]] + ring[line[2]] for line in linepos])) == 1:

                        for line in linepos:
                                string += str(ring[line[0]]) + str(ring[line[1]]) + str(ring[line[2]]) 

                        # filter for length 16
                        if len(string) == 16:
                                #print("found a valid ring", string)
                                maxring = max(maxring, int(string))

print(maxring)