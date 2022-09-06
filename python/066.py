"""
Project Euler Problem 66
========================

Consider quadratic Diophantine equations of the form:

                              x^2 - Dy^2 = 1

For example, when D=13, the minimal solution in x is 649^2 - 13 * 180^2 =
1.

It can be assumed that there are no solutions in positive integers when D
is square.

By finding minimal solutions in x for D = {2, 3, 5, 6, 7}, we obtain the
following:

3^2 - 2 * 2^2 = 1
2^2 - 3 * 1^2 = 1
9^2 - 5 * 4^2 = 1
5^2 - 6 * 2^2 = 1
8^2 - 7 * 3^2 = 1

Hence, by considering minimal solutions in x for D 7, the largest x is
obtained when D=5.

Find the value of D 1000 in minimal solutions of x for which the largest
value of x is obtained.
"""


# Diophantine equations and number theory are like chess.  You can understand the basics quickly, but it takes so much to be good once you start unraveling the connections with complex areas of math. 
# Case in point, the equation above is known as Pell's equation: https://en.wikipedia.org/wiki/Pell%27s_equation 
# I spent over a week learning and researching this.  Mathworld was a great resource on pell's equation: https://mathworld.wolfram.com/PellEquation.html

# There is a bonkers theorem that connects the solution of Pell's equation with the convergentes of continued fractions (WOW!): https://en.wikipedia.org/wiki/Pell%27s_equation#Fundamental_solution_via_continued_fractions
# a nice write up of pell's equation and its solution: https://www.ams.org/notices/200202/fea-lenstra.pdf 


import math, fractions

# return length of period or 0 for perfect squares
# continuedFractionforSqrt(2)  returns a pair (1, [2]).  Period is the length of element (1)
def continuedFractionforSqrt(n):

    #closest perfect square to the square root
    root = a0 = math.isqrt(n)

    cont_fraction = (a0, [])

    # return if n is a perfect square
    if a0 * a0 == n: 
        return cont_fraction

    numerator   = 0 
    denominator = 1  
    period = 0

    while True: 
        numerator   = denominator * a0 - numerator
        denominator = (n - numerator * numerator) // denominator
        a0 = (root + numerator) // denominator

        # iterate until we see the same triplet (a, numerator, denominator) a second time
        # first iteration we store the triple
        # after that we check if next triplet has been seen before
        if period == 0:
            a,den,num = a0, denominator, numerator
        elif (a,den,num) == (a0, denominator, numerator): # if we see the same triplet again, we hit a period
            break

        cont_fraction[1].append(a0)   
        period += 1
    return cont_fraction


# use this algorithm to solve x^2 -Dyˆ2 = 1 (Pells equation)
# https://en.wikipedia.org/wiki/Pell%27s_equation#Fundamental_solution_via_continued_fractions
# D should not be a square
# TODO: the many checks in the loop below could probably be simplied into one or two conditions if we initialize and iterate a list that has both components of the continuous fraction.   
def solvePellEquation(D):

    # return 0 if D is a perfect square (no solution as two squares have > 1 difference between them)
    if D == math.isqrt(D) ** 2:
        return -1, -1

    try:
        cont_fract = continuedFractionforSqrt(D)
        #print("cont frac", cont_fract)

        # since we look at the period minus the last digit, ensure the period is greater than one
        if len(cont_fract[1]) > 1:

            # look at the period minus the last number.  
            frac = fractions.Fraction(cont_fract[1][-2], 1)
            #print("initial frac", frac)

            # for the continuous fraction representation, calculate for each term  t_n + 1 / t_{n+1} and continue iterating 
            for term in reversed(cont_fract[1][: -2]):
                frac = term + 1 / frac 
                #print("iterate on frac:", frac)

            # add the main number
            frac = 1/ frac + cont_fract[0]

            #print("iterate on frac f:", frac)

        # if the period length is one, we only look at the first digit. 
        else:
            frac = fractions.Fraction(cont_fract[0], 1)


        if len(cont_fract[1]) % 2 == 0:
            return frac.numerator, frac.denominator
        else:
            return frac.numerator**2 + frac.denominator**2 * D, 2*frac.numerator * frac.denominator
    except:
        print("error for ", D, cont_fract)
        return -1, -1


maxSol = -1
maxD = -1
for i in range(2, 1001):
    if solvePellEquation(i)[0] > maxSol:
        maxSol = solvePellEquation(i)[0]
        maxD = i
        #print("new max", i, maxSol)

print(maxD)

