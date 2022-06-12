
Euler-a-Day - one Euler Project Problem at a time
===========================================

> "We overestimate how much we can achieve in a day and understimate what we can achieve in a year" -- one of too many blogs out there. 

I love math and coding, and want to see how far I can get solving [Project Euler Problems](https://projecteuler.net) while expanding into optimizing the solution and documenting patterns and findings as I go along.


## Motivation ##

After one year of a daily work out routine, the results have been extraordinary.  It might not feel like a big effort, but it took many false starts to get here.  Boils down to **"do a little bit every day"**.  

This is my attempt at building a similar habit for math + coding.   Why? 

- Build muscle and routine.  How far can I get with doing a problem a day? 
- Document trade offs and what are the best ways to code 
- Compare best practices across approaches and languages (starting with C and Python) .  
- Expand the problems beyond the initial input constrains.  E.g.  Identify patterns if expanding the input space. 


## Why am I sharing my solutions? ## 

If you are looking for a solution to a problem, there are many places out there that will list them.   So, I don't think I'm spoiling it. 

Solving these problems requires:  1- Understand the math problem and translating it into a formula or approach.  2- Convert this appraoch into a coded algorithm to be evaluated.  I claim there's a third step: reflection.   Most of these problems will have more than one way to be solved, leadig to trade offs.  What can I learn from solving these problems in multipe ways? 

# Principles I'm following # 

- Cap work at Max 1 hour x day, weekends off. 
- Googling general concepts (research) is ok, but don't look at others solution to the problem.  
- Commit before checking the work at euler project site and looking at their amazing answers and forum. What you see are my thoughts before seeing the answers. 
- Explanation on approach, pitfalls, performance and thoughts in the comments of each solution 
- Write simplest solution first, then expand to a more optimized one.  Simplest is usually the "brute force approach" as  computers are fast.   
- Run problem for a range of inputs to evaluate performance analysis and scale as appropriate.



# List of problems # 

| Problem       | Python        | C  | Difficulty |  Notes |  
| ------------- | ------------- |------------- |------------- |------------- |
| [001](https://projecteuler.net/problem=1)  | [001.py](python/001.py) | | **Easy** | Problem wasn't hard, took time to set up profiling, github etc.  Brute force approach worked for default input but won't scale for larger inputs. One finding: Naive approach worked better than pythonic code.  |
| [002](https://projecteuler.net/problem=2)  | [002.py](python/002.py) | | **Easy** | So many formulas for Fibonacci additions, Barely got to try one optimization but a lot more there.  Computers are really good at adding large numbers, so not worth optimizing further. |
| [003](https://projecteuler.net/problem=3)  | [003.py](python/003.py) | | **Easy** | The brute force approach can be optimized by reducing the # of factors to try. There are other algorithms like Pollard's algorithm which performs substantially better for larger numbers. |
| [004](https://projecteuler.net/problem=4)  | [004.py](python/004.py) | | **Easy** | Brute force was sufficient for 3 digits, but it won't scale for larger # of digits.  |
| [005](https://projecteuler.net/problem=5)  | [005.py](python/005.py) | | **Easy** | Two intuitive methods: One based on  Euclid's algorithm (GCD), the second an inefficient factorize all numbers in the range and get the maximum exponent for each prime dividing each number in range.  |
| [006](https://projecteuler.net/problem=6)  | [006.py](python/006.py) | | **Easy** | Brute force solves this straightforward, but it won't scale for large numbers.  There are easy formulas for both expressions that yield an immediate result |
| [007](https://projecteuler.net/problem=7)  | [007.py](python/007.py) | | **Easy** | Direct implemenation of a sieve of Erathostenes, and an idea to use a generator which is better suited for this problem.  There's a lot more to optimize here, but will revisit later.   |
| [008](https://projecteuler.net/problem=8)  | [008.py](python/008.py) | | **Easy** | straightforward problem. Good oppoortunity to start with a c style approach and transform to a pythonic one (I got half way there, I'm sure this one can further be compressed).  Pythonic doesn't perform as well as plainly iteratively but for these challenges that doesn't matter.  |
| [009](https://projecteuler.net/problem=9)  | [009.py](python/009.py) | | **Easy** | Fastest problem to solve, done in 2 minutes.  Really simple brute force approach. There are other ways to optimize to be worked on. |
| [010](https://projecteuler.net/problem=10)  | [010.py](python/010.py) | | **Easy** | Two solutions - a prime generating function and a sieve approach - sieve is much faster. |
| [011](https://projecteuler.net/problem=11)  | [011.py](python/011.py) | | **Easy** | Not a lot of math, just an observation that you only have to check 4 directions. |
| [012](https://projecteuler.net/problem=12)  | [012.py](python/012.py) | | **Easy** | Reusing prime generator and factorizing by primes  | 