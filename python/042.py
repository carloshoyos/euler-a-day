"""
Project Euler Problem 42
========================

The n-th term of the sequence of triangle numbers is given by, t[n] =
1/2n(n+1); so the first ten triangle numbers are:

                 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

By converting each letter in a word to a number corresponding to its
alphabetical position and adding these values we form a word value. For
example, the word value for SKY is 19 + 11 + 25 = 55 = t[10]. If the word
value is a triangle number then we shall call the word a triangle word.

Using words.txt, a 16K text file containing nearly two-thousand common
English words, how many are triangle words?
"""

# the longest word has 14  characters, which means the longest triangle number is less than 14*26 = 364
# precalculating triangle numbers in a set to check if a word value is triangular very fast.
import re

triangleNumbers = set([int(0.5 * n * (n+1)  ) for n in range(1,30)])


with open('resources/words.txt', 'r') as f: 
    lines = f.read()

lines = re.findall(r"[\w']+", lines)

def isTriangleWord(word):
    global triangleNumbers
    return sum(ord(c) - ord('A') + 1 for c in word) in triangleNumbers


print( sum([1 for w in lines if isTriangleWord(w)]) )