
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
| [001](https://projecteuler.net/problem=1)  | [001.py](python/001.py) | | **Easy-5%** | Problem wasn't hard, took time to set up profiling, github etc.  Brute force approach worked for default input but won't scale for larger inputs. One finding: Naive approach worked better than pythonic code.  |
| [002](https://projecteuler.net/problem=2)  | [002.py](python/002.py) | | **Easy-5%** | So many formulas for Fibonacci additions, Barely got to try one optimization but a lot more there.  Computers are really good at adding large numbers, so not worth optimizing further. | Fibonacci |
| [003](https://projecteuler.net/problem=3)  | [003.py](python/003.py) | | **Easy-5%** | The brute force approach can be optimized by reducing the # of factors to try. There are other algorithms like Pollard's algorithm which performs substantially better for larger numbers. | factorization | 
| [004](https://projecteuler.net/problem=4)  | [004.py](python/004.py) | | **Easy-5%** | Brute force was sufficient for 3 digits, but it won't scale for larger # of digits.  |
| [005](https://projecteuler.net/problem=5)  | [005.py](python/005.py) | | **Easy-5%** | Two intuitive methods: One based on  Euclid's algorithm (GCD), the second an inefficient factorize all numbers in the range and get the maximum exponent for each prime dividing each number in range.  |
| [006](https://projecteuler.net/problem=6)  | [006.py](python/006.py) | | **Easy-5%** | Brute force solves this straightforward, but it won't scale for large numbers.  There are easy formulas for both expressions that yield an immediate result |
| [007](https://projecteuler.net/problem=7)  | [007.py](python/007.py) | | **Easy-5%** | Direct implemenation of a sieve of Erathostenes, and an idea to use a generator which is better suited for this problem.  There's a lot more to optimize here, but will revisit later.   |
| [008](https://projecteuler.net/problem=8)  | [008.py](python/008.py) | | **Easy-5%** | straightforward problem. Good oppoortunity to start with a c style approach and transform to a pythonic one (I got half way there, I'm sure this one can further be compressed).  Pythonic doesn't perform as well as plainly iteratively but for these challenges that doesn't matter.  |
| [009](https://projecteuler.net/problem=9)  | [009.py](python/009.py) | | **Easy-5%** | Fastest problem to solve, done in 2 minutes.  Really simple brute force approach. There are other ways to optimize to be worked on. |
| [010](https://projecteuler.net/problem=10)  | [010.py](python/010.py) | | **Easy-5%** | Two solutions - a prime generating function and a sieve approach - sieve is much faster. |
| [011](https://projecteuler.net/problem=11)  | [011.py](python/011.py) | | **Easy-5%** | Not a lot of math, just an observation that you only have to check 4 directions. |
| [012](https://projecteuler.net/problem=12)  | [012.py](python/012.py) | | **Easy-5%** | Reusing prime generator and factorizing by primes  | triangle numbers, factorization, divisors| 
| [013](https://projecteuler.net/problem=13)  | [013.py](python/013.py) | | **Easy-5%** | Thanks to Python's int, this can be calculated in one line with no data type headaches  | 
| [014](https://projecteuler.net/problem=14)  | [014.py](python/014.py) | | **Easy-5%** | Two solutions - easy brute force (i.e. calculate each number's sequence), and one caching previous results that is way faster.  | 
| [015](https://projecteuler.net/problem=15)  | [015.py](python/015.py) | | **Easy-5%** | Real nice math problem - easy to visualize the relationship between paths and pascal triangle and combinatorics.  This is such a rich area of "play math" with real world applications.  | 
| [016](https://projecteuler.net/problem=16)  | [016.py](python/016.py) | | **Easy-5%** | This is so easy with Python's data types.  | 
| [017](https://projecteuler.net/problem=17)  | [017.py](python/017.py) | | **Easy-5%** |  Not a hard problem but some prep needed writing numbers in english :(  | 
| [018](https://projecteuler.net/problem=18)  | [018.py](python/018.py) | | **Easy-5%** |  Good advice in problem description, instead of brute force, calculate bottom up max value line by line  | triangle numbers shape, maximum path | 
| [019](https://projecteuler.net/problem=19)  | [019.py](python/019.py) | | **Easy-5%** | Super easy to code although not good, could be generalized  | 
| [020](https://projecteuler.net/problem=20)  | [020.py](python/020.py) | | **Easy-5%** | Python makes this so easy / one liner in 2 minutes coding time. Super easy.   | 
| [021](https://projecteuler.net/problem=21)  | [021.py](python/021.py) | | **Easy-5%** | A simple brute force approach worked better than my initial idea of using primes and divisors from problem 12. Sometimes easier brute force is better.   | 
| [022](https://projecteuler.net/problem=22)  | [022.py](python/022.py) | | **Easy-5%** | Easy iteration coding - example of c style vs pythonic coding.   | dictionary sorting, unicode character value, ascii, ord, file |
| [023](https://projecteuler.net/problem=23)  | [023.py](python/023.py) | | **Easy-5%** | A good building block came from problem 21.    | divisors | 
| [024](https://projecteuler.net/problem=24)  | [024.py](python/024.py) | | **Easy-5%** | Two implementations, brute force and deducing a formula. Performance is the same for smaller numbers, but the formula scales much better for large numbers.    | itertools. |
| [025](https://projecteuler.net/problem=25)  | [025.py](python/025.py) | | **Easy-5%** | Super simple, reusing Fibonacci formula and a counter. | Fibonacci |
| [026](https://projecteuler.net/problem=26)  | [026.py](python/026.py) | | **Easy-5%** | Simple, iterating on a division and reminder algorithm. | Divison |
| [027](https://projecteuler.net/problem=27)  | [027.py](python/027.py) | | **Easy-5%** | This can be solved straightforward by evaluating the solution space. | Primes, polynomial |
| [028](https://projecteuler.net/problem=28)  | [028.py](python/028.py) | | **Easy-5%** | Two approaches, brute force and deriving a formula. Good example of how there are 2 ways to solve these problems | arrays, sums |
| [029](https://projecteuler.net/problem=29)  | [029.py](python/029.py) | | **Easy-5%** | Thanks to Python's auto number type, this was trivial to solve, done in less than a minute |
| [030](https://projecteuler.net/problem=30)  | [030.py](python/030.py) | | **Easy-5%** | Once you estimate an upper bound for this problem, the code is trivial to write.   |
| [031](https://projecteuler.net/problem=31)  | [031.py](python/031.py) | | **Easy-5%** | Multipe ways to solve the change problem, using recursion and dynamic programing.   | recursion, dynamic programming, coin partitions | 
| [032](https://projecteuler.net/problem=32)  | [032.py](python/032.py) | | **Easy-5%** | Brute force works here since the solution space is small.   | pandigital, divisors | 
| [033](https://projecteuler.net/problem=33)  | [033.py](python/033.py) | | **Easy-5%** | Brute force works but the code was tedious to write.  Assuming a simplified approach made for much simpler code.  | digits, strings, fractions | 
| [034](https://projecteuler.net/problem=34)  | [034.py](python/034.py) | | **Easy-5%** | Easy brute force since the solution space is small.  | digits, strings | 
| [035](https://projecteuler.net/problem=35)  | [035.py](python/035.py) | | **Easy-5%** | Simple to test the space by precomputing all primes with a sieve and using a set for speed.    | primes, string cycles | 
| [036](https://projecteuler.net/problem=36)  | [036.py](python/036.py) | | **Easy-5%** | A simple test for each possible number.   | palindromes, binary | 
| [037](https://projecteuler.net/problem=37)  | [037.py](python/037.py) | | **Easy-5%** | Implemented with a sieve, but a quick prime evaluation might be as fast with less code | primes, cycles | 
| [038](https://projecteuler.net/problem=38)  | [038.py](python/038.py) | | **Easy-5%** | Solution space is small enough to just test all options.   | number, concatenation, | 
| [039](https://projecteuler.net/problem=39)  | [039.py](python/039.py) | | **Easy-5%** | Brute force works, but limiting the solution space by noticing answer can only be even improces execution time.   | pitagorean triplets | 
| [040](https://projecteuler.net/problem=40)  | [040.py](python/040.py) | | **Easy-5%** | Python has no problem handling this very long string.   | integer concatenation, file | 
| [041](https://projecteuler.net/problem=41)  | [041.py](python/041.py) | | **Easy-5%** | Two approaches (generate all primes or all pandigital numbers) but only one will work given the size of the solution space.   | pandigital permutations primes| 
| [042](https://projecteuler.net/problem=42)  | [042.py](python/042.py) | | **Easy-5%** | Simple string count manipulation.   | triange numbers, string value, ascii, ord | 
| [043](https://projecteuler.net/problem=43)  | [043.py](python/043.py) | | **Easy-5%** | Reuse pandigital permutations.  Brute force works about 4 seconds, there are ways to reduce the solution space to improve performance   | pandigital permutations primes | 
| [044](https://projecteuler.net/problem=44)  | [044.py](python/044.py) | | **Easy-5%** | Reuse pandigital permutations.  Brute force works about 4 seconds, there are ways to reduce the solution space to improve performance   | pentagonal numbers, combinantions | 
| [045](https://projecteuler.net/problem=45)  | [045.py](python/045.py) | | **Easy-5%** | Brute force  is very fast when precalculating the numbers in a set  | pentagonal numbers | 
| [046](https://projecteuler.net/problem=46)  | [046.py](python/046.py) | | **Easy-5%** | Brute force iteration and test (using itertools or sequentially)  | primes, goldbach square | 
| [047](https://projecteuler.net/problem=47)  | [047.py](python/047.py) | | **Easy-5%** | Reusing problem 3, need a fast factorization to test all combinations  | factorization, pollard factorization | 
| [048](https://projecteuler.net/problem=48)  | [048.py](python/048.py) | | **Easy-5%** | Python auto type allows this to be calculated in one expression.  However, for other languages / larger numbers, using the distributive rule for module to partially calculate the last digits, i.e. x^n mod m = x^(n-1) mod m  * x mod m (continue applying recursively)   | large numbers, modulus and exponential factorization | 
| [049](https://projecteuler.net/problem=49)  | [049.py](python/049.py) | | **Easy-5%** | the problem space is small - (4 digit prime numbers), for this to be brute force calculated.   | sieve, primes, sequences, same digits| 
| [050](https://projecteuler.net/problem=50)  | [050.py](python/050.py) | | **Easy-5%** | Consecutive prime sum. Fairly easy once having an ordered list of prime numbers (sieve)  | sieve, primes, slice sum| 
| [051](https://projecteuler.net/problem=51)  | [051.py](python/051.py) | | **Easy-15%** | brute force approach possible, but the problem won't scale. Nice optimization to narrow down the number of replacements / solution space.   | sieve, primes, replacemeent, same digits| 
| [052](https://projecteuler.net/problem=52)  | [052.py](python/052.py) | | **Easy** | super easy, using set to calculate unique digits of a number | digits of number, cycles| 
| [053](https://projecteuler.net/problem=53)  | [053.py](python/053.py) | | **Easy** | Surprising python was able to calculate with brute force, although a binomial formula scales better.   | combinatorics, factorial, pascal triangle, binomical| 
| 54 | - | | **Easy** | ... pending, this is a tedious / long and non mathematical, although some interesting data structures can be used  | | 
| [055](https://projecteuler.net/problem=55)  | [055.py](python/055.py) | | **Easy** | Very simple iteration, not many ways to optimize. Solved in pythonic and non pythinc style.   | Lychrel, palindromic| 
| [056](https://projecteuler.net/problem=56)  | [056.py](python/056.py) | | **Easy** | While multiplication leads to very large numbers, python auto type made this trivial using brute force   | exponents, digits| 
| [057](https://projecteuler.net/problem=57)  | [057.py](python/057.py) | | **Easy** | Easy once you find a formula for the expanding fraction.  |expanding fractions | 
| [058](https://projecteuler.net/problem=58)  | [058.py](python/058.py) | | **Easy** | Easy once you find a formula for the diagonals in the spiral  |spirals, primes | 
| [059](https://projecteuler.net/problem=59)  | [059.py](python/059.py) | | **Easy** | This one has multiple ways to solving depending on accuracy. I just tested first charaacters against english letter popularity distribution, but its possible to craft an input that would have broken that approach.  | cypher, xor, text, English, letter distribution| 
| [060](https://projecteuler.net/problem=60)  | [060.py](python/060.py) | | **Easy-20%** | Great problem, more complex than previous. By estimating the problem space and caching pairs of swappable primes, we can find the chain efficiently using recursion.  | primes, chains, graphs, recursion, | 
| [061](https://projecteuler.net/problem=61)  | [061.py](python/061.py) | | **Easy-20%** | Similar to problem 60. Another use of recursion for backtracking / expanding a chain.   | polygonal numbers, chains, graphs, recursion, | 
| [062](https://projecteuler.net/problem=62)  | [062.py](python/062.py) | | **Easy-15%** | A good example of how when a first obvious approach won't work, but there's a simple alternative that performs really well.    | cubes, digits, combinations | 
| [063](https://projecteuler.net/problem=63)  | [063.py](python/063.py) | | **Easy%** | after the last 3, this one was very easy. Just had to narrow down the solution space, and was able to brute force it| **Easy** |    | digits, powers | 
| [064](https://projecteuler.net/problem=64)  | [064.py](python/064.py) | | **Easy-20%** |  This one took a few days to come up with a formula. Pen and paper and wikipedia.  | continuous fractions, squares | 
| [065](https://projecteuler.net/problem=65)  | [065.py](python/065.py) | | **Easy-15%** |  I thougth writing a continuous function generator  in the previous problem would help, but this was a different approach.  Still, a lot of the lifting was done before, so it wasn't as hard.  | continuous fractions, squares, exp | 
| [066](https://projecteuler.net/problem=66)  | [066.py](python/066.py) | | **Easy-25%** |  Mind blown that you can use continuous fractions to solve a specific dyophantine equation (Pell's equation). A naive approach would never work. This was a hell of a problem, I spend close to two weeks learning about Pell and continuous fractions. | continuous fractions, Pell's equation, dyophantine | 
| [067](https://projecteuler.net/problem=67)  | [067.py](python/067.py) | | **Easy-5%** |  Afte one week of struggling with the last ones, this was a good break. Reusing problem 18 solved fairly quickly. Just check that the input file had an extra  new line. | triangle numbers shape, maximum path |  
| [068](https://projecteuler.net/problem=68)  | [068.py](python/068.py) | | **Easy-25%** |  eventhough this one is a 25%, its much easier than the last one of this difficulty. The right data structure and brute force made this a fairly easy problem.  Pen and paper to sketch this at first were essential!! | n-gon rings, 5-gon ring, magic ring.  |  
| [069](https://projecteuler.net/problem=69)  | [069.py](python/069.py) | | **Easy-10%** |  beautiful problem. Phi has so many properties, found 4 different ways to solve this problem. | totient function, phi function, gcd.  |  
| [070](https://projecteuler.net/problem=70)  | [070.py](python/070.py) | | **Easy-10%** |  reusing problem 70, this is a straightforward validation of phi values and a sieve  | phi, totient, euler function, digit permutation, sieve  |
| [071](https://projecteuler.net/problem=71)  | [071.py](python/071.py) | | **Easy-10%** |  Using simple arithmetic, was able to simplify the problem to test only one condition per digit.  Brute force iterate over the simplified problem to find the answer.  | integer fractions, reduced proper fraction  |
| [072](https://projecteuler.net/problem=72)  | [072.py](python/072.py) | | **Easy-20%** |  Connecting dots, the totient phi function helps counting reduced fractions.  | integer fractions, reduced proper fraction, phi, totient  |
| [073](https://projecteuler.net/problem=73)  | [073.py](python/073.py) | | **Easy-15%** |  Using simple arithmetic, was able to simplify the problem to test only one condition per digit.  Brute force iterate over the simplified problem to find the answer.  | integer fractions, reduced proper fraction, farey sequence, the stern-brocot tree|
| [074](https://projecteuler.net/problem=74)  | [074.py](python/074.py) | | **Easy-15%** |  Easy problem can be solved brute force, but creating a cache of precomputed chains was 20x faster.   | sum of the factorial of digits, chains, caching  |
| [075](https://projecteuler.net/problem=75)  | [075.py](python/075.py) | | **Easy-25%** |  This was a real easy problem for a 25% difficulty. Just had to find the right parametrization formula (euclid formula).  | pitagorean triplets, euclid formula for pitagorean triplets, integer squares  |
| [076](https://projecteuler.net/problem=76)  | [076.py](python/076.py) | | **Easy-10%** |  love this problem, many ways to solve (dynamic programming, recursion). Problem 31 solved a simpler version of this.   | partition function, dynamic programming, counting, ways to add up to an integer  |
| [077](https://projecteuler.net/problem=77)  | [077.py](python/077.py) | | **Easy-25%** |  Another version of 77, great pen and paper exercise to try multiple approaches.  Not sure why this one is 25% difficulty when 76 was 10%  | partition function, dynamic programming, counting, ways to add up to an integer  |
| [078](https://projecteuler.net/problem=78)  | [078.py](python/078.py) | | **Easy-30%** |  First 30% difficulty problem. This one was hard unless you knew the partition generation function.  Was able to solve with partition in a few seconds, or reusing problem 76 in 5 minutes.   | euler partition function, dynamic programing, cache  |
| [079](https://projecteuler.net/problem=79)  | [079.py](python/079.py) | | **Easy-10%** |  pending  | ,  |
| [080](https://projecteuler.net/problem=80)  | [080.py](python/080.py) | | **Easy-10%** |  pending  | ,  |
| [081](https://projecteuler.net/problem=81)  | [081.py](python/081.py) | | **Easy-10%** |  pending  | ,  |
| [082](https://projecteuler.net/problem=82)  | [082.py](python/082.py) | | **Easy-10%** |  pending  | ,  |
| [083](https://projecteuler.net/problem=83)  | [083.py](python/083.py) | | **Easy-10%** |  pending  | ,  |
| [084](https://projecteuler.net/problem=84)  | [084.py](python/084.py) | | **Easy-10%** |  pending  | ,  |
| [085](https://projecteuler.net/problem=85)  | [085.py](python/085.py) | | **Easy-10%** |  pending  | ,  |
| [086](https://projecteuler.net/problem=86)  | [086.py](python/086.py) | | **Easy-10%** |  pending  | ,  |
| [087](https://projecteuler.net/problem=87)  | [087.py](python/087.py) | | **Easy-10%** |  pending  | ,  |
| [088](https://projecteuler.net/problem=88)  | [088.py](python/088.py) | | **Easy-10%** |  pending  | ,  |
| [089](https://projecteuler.net/problem=89)  | [089.py](python/089.py) | | **Easy-10%** |  pending  | ,  |
| [090](https://projecteuler.net/problem=90)  | [090.py](python/090.py) | | **Easy-10%** |  pending  | ,  |
| [091](https://projecteuler.net/problem=91)  | [091.py](python/091.py) | | **Easy-10%** |  pending  | ,  |
| [092](https://projecteuler.net/problem=92)  | [092.py](python/092.py) | | **Easy-10%** |  pending  | ,  |
| [093](https://projecteuler.net/problem=93)  | [093.py](python/093.py) | | **Easy-10%** |  pending  | ,  |
| [094](https://projecteuler.net/problem=94)  | [094.py](python/094.py) | | **Easy-10%** |  pending  | ,  |
| [095](https://projecteuler.net/problem=95)  | [095.py](python/095.py) | | **Easy-10%** |  pending  | ,  |
| [096](https://projecteuler.net/problem=96)  | [096.py](python/096.py) | | **Easy-10%** |  pending  | ,  |
| [097](https://projecteuler.net/problem=97)  | [097.py](python/097.py) | | **Easy-10%** |  pending  | ,  |
| [098](https://projecteuler.net/problem=98)  | [098.py](python/098.py) | | **Easy-10%** |  pending  | ,  |
| [099](https://projecteuler.net/problem=99)  | [099.py](python/099.py) | | **Easy-10%** |  pending  | ,  |