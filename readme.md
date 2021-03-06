
Euler-a-Day - one Euler Project Problem at a time
===========================================

> "We overestimate how much we can achieve in a day and understimate what we can achieve in a year" -- one of too many blogs out there. 

I love math and coding, and want to see how far I can get solving [Project Euler Problems](https://projecteuler.net) while expanding into optimizing the solution and documenting patterns and findings as I go along.


## Motivation ##

In the last year I have built an exercise routine where the habit of daily work outs has become entrenched with extraordinary results.  Thnking about previous false starts, the key for success boils down to **"do a little bit every day"**.  

This is my attempt at building a similar habit for math + coding.   Why? 

- Build muscle and routine.  How far can I get with doing a problem a day? 
- Document trade offs and what are the best ways to code 
- Compare best practices across approaches and languages (starting with C and Python) .  
- Expand the problems beyond the initial input constrains.  E.g.  Identify patterns if expanding the input space. 


## Why am I sharing my solutions? ## 

Euler project is ok with sharing the first 100 solutions, and this keep me accountable. Plus, there are many other solutions repo out there.  

I expect to provide insights as I go along.  After problem 100, I'll only include the insights but not the solution.

Solving these problems requires:  1- Understand the math problem and translating it into a formula or approach.  2- Convert this appraoch into a coded algorithm to be evaluated. 3- reflection.   Most of these problems will have more than one way to be solved, leadig to trade offs.  What can I learn from solving these problems in different ways?  

# Principles I'm following # 

- Cap work at Max 1 hour x day, weekends off. 
- Googling general concepts (research) is ok, but don't look at others solution to the problem.  
- Commit before checking the work at euler project site and looking at their amazing answers and forum. What you see are my thoughts before seeing the answers. 
- Explanation on approach, pitfalls, performance and thoughts in the comments of each solution 
- Write simplest solution first, then expand to a more optimized one.  Simplest is usually the "brute force approach" as  computers are fast.   
- Run problem for a range of inputs to evaluate performance analysis and scale as appropriate.


# List of problems # 

| Problem       | Python        | C  | Difficulty |  Notes |  Keyword | 
| ------------- | ------------- |------------- |------------- |------------- |------------- |
| [001](https://projecteuler.net/problem=1)  | [001.py](python/001.py) | | **Easy** | Problem wasn't hard, took time to set up profiling, github etc.  Brute force approach worked for default input but won't scale for larger inputs. One finding: Naive approach worked better than pythonic code.  |
| [002](https://projecteuler.net/problem=2)  | [002.py](python/002.py) | | **Easy** | So many formulas for Fibonacci additions, Barely got to try one optimization but a lot more there.  Computers are really good at adding large numbers, so not worth optimizing further. | Fibonacci |
| [003](https://projecteuler.net/problem=3)  | [003.py](python/003.py) | | **Easy** | The brute force approach can be optimized by reducing the # of factors to try. There are other algorithms like Pollard's algorithm which performs substantially better for larger numbers. | factorization | 
| [004](https://projecteuler.net/problem=4)  | [004.py](python/004.py) | | **Easy** | Brute force was sufficient for 3 digits, but it won't scale for larger # of digits.  |
| [005](https://projecteuler.net/problem=5)  | [005.py](python/005.py) | | **Easy** | Two intuitive methods: One based on  Euclid's algorithm (GCD), the second an inefficient factorize all numbers in the range and get the maximum exponent for each prime dividing each number in range.  |
| [006](https://projecteuler.net/problem=6)  | [006.py](python/006.py) | | **Easy** | Brute force solves this straightforward, but it won't scale for large numbers.  There are easy formulas for both expressions that yield an immediate result |
| [007](https://projecteuler.net/problem=7)  | [007.py](python/007.py) | | **Easy** | Direct implemenation of a sieve of Erathostenes, and an idea to use a generator which is better suited for this problem.  There's a lot more to optimize here, but will revisit later.   |
| [008](https://projecteuler.net/problem=8)  | [008.py](python/008.py) | | **Easy** | straightforward problem. Good oppoortunity to start with a c style approach and transform to a pythonic one (I got half way there, I'm sure this one can further be compressed).  Pythonic doesn't perform as well as plainly iteratively but for these challenges that doesn't matter.  |
| [009](https://projecteuler.net/problem=9)  | [009.py](python/009.py) | | **Easy** | Fastest problem to solve, done in 2 minutes.  Really simple brute force approach. There are other ways to optimize to be worked on. |
| [010](https://projecteuler.net/problem=10)  | [010.py](python/010.py) | | **Easy** | Two solutions - a prime generating function and a sieve approach - sieve is much faster. |
| [011](https://projecteuler.net/problem=11)  | [011.py](python/011.py) | | **Easy** | Not a lot of math, just an observation that you only have to check 4 directions. |
| [012](https://projecteuler.net/problem=12)  | [012.py](python/012.py) | | **Easy** | Reusing prime generator and factorizing by primes  | triangle numbers, factorization, divisors| 
| [013](https://projecteuler.net/problem=13)  | [013.py](python/013.py) | | **Easy** | Thanks to Python's int, this can be calculated in one line with no data type headaches  | 
| [014](https://projecteuler.net/problem=14)  | [014.py](python/014.py) | | **Easy** | Two solutions - easy brute force (i.e. calculate each number's sequence), and one caching previous results that is way faster.  | 
| [015](https://projecteuler.net/problem=15)  | [015.py](python/015.py) | | **Easy** | Real nice math problem - easy to visualize the relationship between paths and pascal triangle and combinatorics.  This is such a rich area of "play math" with real world applications.  | 
| [016](https://projecteuler.net/problem=16)  | [016.py](python/016.py) | | **Easy** | This is so easy with Python's data types.  | 
| [017](https://projecteuler.net/problem=17)  | [017.py](python/017.py) | | **Easy** |  Not a hard problem but some prep needed writing numbers in english :(  | 
| [018](https://projecteuler.net/problem=18)  | [018.py](python/018.py) | | **Easy** |  Good advice in problem description, instead of brute force, calculate bottom up max value line by line  | 
| [019](https://projecteuler.net/problem=19)  | [019.py](python/019.py) | | **Easy** | Super easy to code although not good, could be generalized  | 
| [020](https://projecteuler.net/problem=20)  | [020.py](python/020.py) | | **Easy** | Python makes this so easy / one liner in 2 minutes coding time. Super easy.   | 
| [021](https://projecteuler.net/problem=21)  | [021.py](python/021.py) | | **Easy** | A simple brute force approach worked better than my initial idea of using primes and divisors from problem 12. Sometimes easier brute force is better.   | 
| [022](https://projecteuler.net/problem=22)  | [022.py](python/022.py) | | **Easy** | Easy iteration coding - example of c style vs pythonic coding.   | dictionary sorting, unicode character value |
| [023](https://projecteuler.net/problem=23)  | [023.py](python/023.py) | | **Easy** | A good building block came from problem 21.    | divisors | 
| [024](https://projecteuler.net/problem=24)  | [024.py](python/024.py) | | **Easy** | Two implementations, brute force and deducing a formula. Performance is the same for smaller numbers, but the formula scales much better for large numbers.    | itertools. |
| [025](https://projecteuler.net/problem=25)  | [025.py](python/025.py) | | **Easy** | Super simple, reusing Fibonacci formula and a counter. | Fibonacci |
| [026](https://projecteuler.net/problem=26)  | [026.py](python/026.py) | | **Easy** | Simple, iterating on a division and reminder algorithm. | Divison |
| [027](https://projecteuler.net/problem=27)  | [027.py](python/027.py) | | **Easy** | This can be solved straightforward by evaluating the solution space. | Primes, polynomial |
| [028](https://projecteuler.net/problem=28)  | [028.py](python/028.py) | | **Easy** | Two approaches, brute force and deriving a formula. Good example of how there are 2 ways to solve these problems | arrays, sums |
| [029](https://projecteuler.net/problem=29)  | [029.py](python/029.py) | | **Easy** | Thanks to Python's auto number type, this was trivial to solve, done in less than a minute |
| [030](https://projecteuler.net/problem=30)  | [030.py](python/030.py) | | **Easy** | Once you estimate an upper bound for this problem, the code is trivial to write.   |
| [031](https://projecteuler.net/problem=31)  | [031.py](python/031.py) | | **Easy+** | Multipe ways to solve the change problem, using recursion and dynamic programing.   | recursion, dynamic programming | 
| [032](https://projecteuler.net/problem=32)  | [032.py](python/032.py) | | **Easy** | Brute force works here since the solution space is small.   | pandigital, divisors | 
| [033](https://projecteuler.net/problem=33)  | [033.py](python/033.py) | | **Easy** | Brute force works but the code was tedious to write.  Assuming a simplified approach made for much simpler code.  | digits, strings | 
| [034](https://projecteuler.net/problem=34)  | [034.py](python/034.py) | | **Easy** | Easy brute force since the solution space is small.  | digits, strings | 
| [035](https://projecteuler.net/problem=35)  | [035.py](python/035.py) | | **Easy** | Simple to test the space by precomputing all primes with a sieve and using a set for speed.    | primes, string cycles | 
| [036](https://projecteuler.net/problem=36)  | [036.py](python/036.py) | | **Easy** | A simple test for each possible number.   | palindromes, binary | 
| [037](https://projecteuler.net/problem=37)  | [037.py](python/037.py) | | **Easy** | Implemented with a sieve, but a quick prime evaluation might be as fast with less code | primes, cycles | 
| [038](https://projecteuler.net/problem=38)  | [038.py](python/038.py) | | **Easy** | Solution space is small enough to just test all options.   | number, concatenation, | 
| [039](https://projecteuler.net/problem=39)  | [039.py](python/039.py) | | **Easy** | Brute force works, but limiting the solution space by noticing answer can only be even improces execution time.   | pitagorean triplets | 
| [040](https://projecteuler.net/problem=40)  | [040.py](python/040.py) | | **Easy** | Python has no problem handling this very long string.   | integer concatenation | 
| [041](https://projecteuler.net/problem=41)  | [041.py](python/041.py) | | **Easy** | Two approaches (generate all primes or all pandigital numbers) but only one will work given the size of the solution space.   | pandigital permutations primes| 
| [042](https://projecteuler.net/problem=42)  | [042.py](python/042.py) | | **Easy** | Simple string count manipulation.   | triange numbers, string value | 
| [043](https://projecteuler.net/problem=43)  | [043.py](python/043.py) | | **Easy** | Reuse pandigital permutations.  Brute force works about 4 seconds, there are ways to reduce the solution space to improve performance   | pandigital permutations primes | 
| [044](https://projecteuler.net/problem=44)  | [044.py](python/044.py) | | **Easy** | Reuse pandigital permutations.  Brute force works about 4 seconds, there are ways to reduce the solution space to improve performance   | pentagonal numbers, combinantions | 
| [045](https://projecteuler.net/problem=45)  | [045.py](python/045.py) | | **Easy** | Brute force  is very fast when precalculating the numbers in a set  | pentagonal numbers | 
| [046](https://projecteuler.net/problem=46)  | [046.py](python/046.py) | | **Easy** | Brute force iteration and test (using itertools or sequentially)  | primes, goldbach square | 
| [047](https://projecteuler.net/problem=47)  | [047.py](python/047.py) | | **Easy** | Reusing problem 3, need a fast factorization to test all combinations  | factorization, pollard factorization | 