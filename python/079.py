"""
Project Euler Problem 79
========================

A common security method used for online banking is to ask the user for
three random characters from a passcode. For example, if the passcode was
531278, they may asked for the 2nd, 3rd, and 5th characters; the expected
reply would be: 317.

The text file keylog.txt contains fifty successful login attempts.

Given that the three characters are always asked for in order, analyse the
file so as to determine the shortest possible secret passcode of unknown
length.
"""


# its unclear if a digit is used more than once.  My first assumption was that each digit is used only once which led to a valid answer.  
# approach 
# a) generate all candidates (by looking at all permutations of the unique digits) and check if the permutation matches all rules
# b) pull all rules into a map that can be traversed:  for example, if rule id ABC, then create a list like [A => [], B -> [A],  

import re
import itertools

with open('resources/keylog.txt') as f:
    rules = f.read().splitlines()
    #lines = f.read()
    
# rules = sorted(re.findall(r"[\w']+", lines))

# get digits in secret passcode
digits = sorted(list(set([x for y in rules for x in y])))


## approach a - #################
#  generate all of the combinations for the digits in the rules, starting with the smallest one
#  validate that the generated passcode matches all rules and stop on first match.  



### return TRUE if the passcode matches all rules. 
### rules is a list of strings and this function 
### for example rules = ['129', '160'], then 12960 will return TRUE (b/c 129 and 160 are sequences found in 12960)
def matchesAllRules(passcode, rules):
    for rule in rules:
        pos = 0
        for d in rule: 
            posnext = passcode.find(d)
            if posnext < pos: return False
            pos = posnext
            
    return True


for comb in itertools.permutations(digits, len(digits)):
    #print(comb)
    if matchesAllRules(''.join(comb), rules):
        print(''.join(comb))
        break


## approach b - #################
#  generate a map of rules..  for each digit pos, keep track in a set of which digits have to come before pos. 
#  if the rules are deterministic, there must be one digit that has no digits before.  
#  Start with that digit as the first one in the passcode. Adjust the rules to remove that digit and iterate until all digits are done. 

rulepath = { x: set() for x in digits}
for rule in rules:
    for idx in range(0, len(rule)-1):
        pre = rule[idx]
        pos = rule[idx+1]
        rulepath[pos].add(pre)


# if the rules are deterministic, there's always be going to be one number that doesn't have any numbers before. 
# recursively iterate through rules to find the one digit that has no numbers before, and use it to assemble the strings
# continue until there are no more rules
# returns None if there is no 

def generatePasscode(passcode, rulepath):
    if len(rulepath) == 0:
        return passcode 
    else:
        for (dig, pres) in rulepath.items():
            #print("checking", dig, pres, passcode.find(dig), len(pres - set(passcode)))
            if passcode.find(dig) == -1 and len(pres - set(passcode)) == 0:
                del rulepath[dig]
                return generatePasscode(passcode + dig, rulepath)
        return None # rules are not deterministic...  



#print(rulepath)
print(generatePasscode('', rulepath))