"""
Project Euler Problem 33
========================

The fraction 49/98 is a curious fraction, as an inexperienced
mathematician in attempting to simplify it may incorrectly believe that
49/98 = 4/8, which is correct, is obtained by cancelling the 9s.

We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

There are exactly four non-trivial examples of this type of fraction, less
than one in value, and containing two digits in the numerator and
denominator.

If the product of these four fractions is given in its lowest common
terms, find the value of the denominator.
"""


from fractions import Fraction

# approach 1 - a hacky approach, since problem states there are 4 solutions, calculate all ab / bc fractions that are less than 1 
# since the result found the 4 relevant fractions, we know this works. 
#    16 / 64, 19 / 95, 26 / 65, 49 / 98

def calculate_hacky():
    product_num = product_den = 1 
    for a in range(1, 10):
        for b in range(1,10):
            for c in range(1,10):
                if (a*10 + b < b*10 + c) and ( (a*10 + b) / (b*10 + c) == a / c):
                    product_num *= a
                    product_den *= c
                #print(a*10 + b , '/',  b*10 + c)  # used this to check that this hacky approach found 4 solutions

    return Fraction(product_num,product_den).denominator # could have calculated gcd but Fraction module does this 

# # approach 2, brute force calculate all 2 digit fractions < 1 and find digit in common and 
# two trivial cases we can skip: 
#  1- fractions with 2 digits in common (e.g.  of the form ab / ba ) won't be valid as the simplification == 1 and the only valid solution is a==b which is not covered. 
#  2- fractions where either numerator or denominator has same digits (e.g. aa/ab)


def calculate_bruteforce():
    product_num = product_den = 1 
    for num in range(11, 100):  # start at 11, as 0 is trivial
        if num % 10 == 0 or num % 11 == 0 : continue
        for den in range(num+1, 100):
            if den % 10 == 0 or den % 11 == 0: continue

            common = set(str(den)) & set(str(num))
            if len(common) == 1:
                    common_d = common.pop() # only one digit common 

                    den_unique = [int(x) for x in str(den) if x != common_d][0]  # find the digit that is unique
                    nom_unique = [int(x) for x in str(num) if x != common_d][0]  # find the digit that is unique

                    if (nom_unique * den ==  num * den_unique):
                        product_num *= num
                        product_den *= den
                        #print("found", num, den, den_unique)
    return Fraction(product_num,product_den).denominator

print(calculate_hacky())
print(calculate_bruteforce())
