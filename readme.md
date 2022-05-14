
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
- Googling is ok, but don't look at someone else's solution.  
- Explanation on approach, pitfalls, performance and thoughts in the comments of each solution 
- Write simplest solution first, then expand to a more optimized one.  Simplest might mean "brute force" cause computers are fast.  
- Run performance analysis for each solution.  
- Include optional parameters to overwrite the input or select different solution approach.   
- For most solutions that have a numeric input, run it with larger numbers to understand how it scales. 



# List of problems # 

| Problem       | Python        | C  | Difficulty |  Notes |  
| ------------- | ------------- |------------- |------------- |------------- |
| [001](https://projecteuler.net/problem=1)  | [001.py](python/001.py) | | **Easy** | Problem wasn't hard, took time to set up profiling, github etc.  Brute force approach worked for default input but won't scale for larger inputs. One finding: Naive approach worked better than pythonic code.  |
| [002](https://projecteuler.net/problem=2)  | [002.py](python/002.py) | | **Easy** | So many formulas for Fibonacci additions, I barely got to try one optimization but a lot more there.  Computers are really good at adding large numbers, so not worth optimizing further. |
