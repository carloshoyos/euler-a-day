"""
Project Euler Problem 65
========================

The square root of 2 can be written as an infinite continued fraction.

2 = 1 +          1
        2 +        1
            2 +      1
                2 +    1
                    2 + ...

The infinite continued fraction can be written, 2 = [1;(2)], (2) indicates
that 2 repeats ad infinitum. In a similar way, 23 = [4;(1,3,1,8)].

It turns out that the sequence of partial values of continued fractions
for square roots provide the best rational approximations. Let us consider
the convergents for 2.

1 + 1 = 3/2
    2

1 +   1   = 7/5
    2 + 1
        2

1 +     1     = 17/12
    2 +   1
        2 + 1
            2

1 +       1       = 41/29
    2 +     1
        2 +   1
            2 + 1
                2

Hence the sequence of the first ten convergents for 2 are:
1, 3/2, 7/5, 17/12, 41/29, 99/70, 239/169, 577/408, 1393/985, 3363/2378,
...

What is most surprising is that the important mathematical constant,
e = [2; 1,2,1, 1,4,1, 1,6,1 , ... , 1,2k,1, ...].

The first ten terms in the sequence of convergents for e are:
2, 3, 8/3, 11/4, 19/7, 87/32, 106/39, 193/71, 1264/465, 1457/536, ...

The sum of digits in the numerator of the 10th convergent is 1+4+5+7=17.

Find the sum of digits in the numerator of the 100th convergent of the
continued fraction for e.
"""

# I thought I could reuse the previous problem, but this one didn't need a formula for the continued fraction, instead its more of a fraction simplification.
# a little bit of mucking around with recurring the formula f(a,b) = a + 1/b and passing the series 2,1,2,1,1,4,1,1,6,1,...  did the trick
# I'm sure there is a more elegant way to implement this. 


from fractions import Fraction

# generate the convergents 
x = [2] + [((d+1)//3)*2 if (d+1)%3 == 0 else 1 for d in range(1,20)]


def get_nth_fraction(n):
    """
    Returns the fraction of the nth convergent of the continued fraction for e.
    """

    n = n -2  # lazy, I should normalize all indexes
    # generate the series 2,1,2,1,1,4,1,... 1,2k,1,..
    x = [2] + [((d+1)//3)*2 if (d+1)%3 == 0 else 1 for d in range(1,n+2)]


    f = x[n] + Fraction(1, x[n+1])
    for i in range(n-1, -1, -1):
        f = x[i] + Fraction(1, f)
    return f


frac  = get_nth_fraction(100)
print(sum([int(i) for i in str(frac.numerator)]))