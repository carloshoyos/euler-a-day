"""
Project Euler Problem 38
========================

Take the number 192 and multiply it by each of 1, 2, and 3:

  192 * 1 = 192
  192 * 2 = 384
  192 * 3 = 576

By concatenating each product we get the 1 to 9 pandigital, 192384576. We
will call 192384576 the concatenated product of 192 and (1,2,3)

The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4,
and 5, giving the pandigital, 918273645, which is the concatenated product
of 9 and (1,2,3,4,5).

What is the largest 1 to 9 pandigital 9-digit number that can be formed as
the concatenated product of an integer with (1,2, ... , n) where n > 1?
"""

# since n > 1, the max range to evaluate is four digits (abcd 2xabcd )
# iterate through those 4, and only calculate digits 1,2,3... until the product has less than 9 digits

def getLargestPandigital():
  ans = ""
  for n in range(1, 10000):
    for d in range(2,9):  # the only pan digital number with (1,..9) is 1, so we can ignore 9.
      result = "".join(str(n * j) for j in range(1, d))

      # if pandigit has more than 10 digits, skip to next number 
      if len(result) > 9:
        break
      if "".join(sorted(result)) == "123456789" and result > ans:
        ans = result
  return ans


print(getLargestPandigital())

