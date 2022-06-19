"""
Project Euler Problem 22
========================

Using names.txt, a 46K text file containing over five-thousand first names,
begin by sorting it into alphabetical order. Then working out the
alphabetical value for each name, multiply this value by its alphabetical
position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, which
is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So,
COLIN would obtain a score of 938 * 53 = 49714.

What is the total of all the name scores in the file?
"""

# the challenge was to read the file and put it in a file. Once that's done, enumerate makes it real easy. 
# two ways to code it, first one is more c style nested loops, the other one is a one liner pythonic example 

import re

with open('resources/names.txt') as f:
    lines = f.read()
    
lines = re.findall(r"[\w']+", lines)



totalval = 0 
#lines = ['COLIN', 'ZOLA']  # test 

# option 1, two nested fors to iterate through words and letters 

for i,n in enumerate(sorted(lines)):
    charval = 0
    for char in n:
        charval += ord(char) - ord('A') + 1
    totalval += (i+1) * charval
    #print(i, n, charval)
print(totalval)


# # option 2, more pythonic the two nested fors are inside a list comprehension. 
totalval = sum((i + 1) * (ord(char) - ord('A') + 1)
    for (i, n) in enumerate(sorted(lines))
    for char in n 
)
print(totalval)
