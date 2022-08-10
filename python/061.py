"""
Project Euler Problem 61
========================

Triangle, square, pentagonal, hexagonal, heptagonal, and octagonal numbers
are all figurate (polygonal) numbers and are generated by the following
formulae:

Triangle     P[3,n]=n(n+1)/2    1, 3, 6, 10, 15, ...
Square       P[4,n]=n^2         1, 4, 9, 16, 25, ...
Pentagonal   P[5,n]=n(3n-1)/2   1, 5, 12, 22, 35, ...
Hexagonal    P[6,n]=n(2n-1)     1, 6, 15, 28, 45, ...
Heptagonal   P[7,n]=n(5n-3)/2   1, 7, 18, 34, 55, ...
Octagonal    P[8,n]=n(3n-2)     1, 8, 21, 40, 65, ...

The ordered set of three 4-digit numbers: 8128, 2882, 8281, has three
interesting properties.

 1. The set is cyclic, in that the last two digits of each number is the
    first two digits of the next number (including the last number with
    the first).
 2. Each polygonal type: triangle (P[3,127]=8128), square (P[4,91]=8281),
    and pentagonal (P[5,44]=2882), is represented by a different number in
    the set.
 3. This is the only set of 4-digit numbers with this property.

Find the sum of the only ordered set of six cyclic 4-digit numbers for
which each polygonal type: triangle, square, pentagonal, hexagonal,
heptagonal, and octagonal, is represented by a different number in the
set.
"""

# another recursive function to grow chains by backtracking at possible candidates until getting to size.  
# start with generating sets for polygon numbers.  
# 



import itertools as it


def polyg_numbers(start, end, formula):

   numbers = []
   for n in it.count(1):
      num = formula(n)
      if start <= num <= end: 
         numbers.append(num)
      if num >= end: 
         break
   return numbers


p3 = polyg_numbers(1000, 10000, lambda n : n * (n + 1) // 2)
p4 = polyg_numbers(1000, 10000, lambda n : n * n)
p5 = polyg_numbers(1000, 10000, lambda n : n * (3 * n - 1) // 2)
p6 = polyg_numbers(1000, 10000, lambda n : n * (2 * n - 1))
p7 = polyg_numbers(1000, 10000, lambda n : n * (5 * n - 3) // 2)
p8 = polyg_numbers(1000, 10000, lambda n : n * (3 * n - 2))


def find_loop(lists, start, end, found_numbers = []):
    if len(lists) == 1 and start * 100 + end in lists[0]:
      found_numbers += [start * 100 + end]  
      print(sum(found_numbers)) # 
      return
    
    for cur_list in lists:
        for c in cur_list:
            if c // 100 == start:
                lists_copy = list(lists) 
                lists_copy.remove(cur_list)
                find_loop(lists_copy, c % 100, end, found_numbers + [c])

for n in p8:
    find_loop([p3, p4, p5, p6, p7], n % 100, n // 100, [n])
