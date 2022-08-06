"""
Project Euler Problem 59
========================

Each character on a computer is assigned a unique code and the preferred
standard is ASCII (American Standard Code for Information Interchange).
For example, uppercase A = 65, asterisk (*) = 42, and lowercase k = 107.

A modern encryption method is to take a text file, convert the bytes to
ASCII, then XOR each byte with a given value, taken from a secret key. The
advantage with the XOR function is that using the same encryption key on
the cipher text, restores the plain text; for example, 65 XOR 42 = 107,
then 107 XOR 42 = 65.

For unbreakable encryption, the key is the same length as the plain text
message, and the key is made up of random bytes. The user would keep the
encrypted message and the encryption key in different locations, and
without both "halves", it is impossible to decrypt the message.

Unfortunately, this method is impractical for most users, so the modified
method is to use a password as a key. If the password is shorter than the
message, which is likely, the key is repeated cyclically throughout the
message. The balance for this method is using a sufficiently long password
key for security, but short enough to be memorable.

Your task has been made easy, as the encryption key consists of three
lower case characters. Using cipher1.txt, a file containing the encrypted
ASCII codes, and the knowledge that the plain text must contain common
English words, decrypt the message and find the sum of the ASCII values
in the original text.
"""

# approach 1 - look at all combinations from aaa to zzz and decrypt.  
# the decrypted data should be common english words. By looking at letter distribution, there should be almost no non a-z characters. 
# using this distribution to do a scoring algorithm of the decryption: https://www3.nd.edu/~busiforc/handouts/cryptography/letterfrequencies.html
# optimization idea - don't decrpyt the whole string, only the first x characters 

import itertools


# applies xor for the key to the text and returns decrypted numbers
def decrypt(text, key):
	return [(letter ^ key[i % len(key)]) for (i, letter) in enumerate(text)]


def score_string(text):
    # if in 'eariotnsl', add 4 
    # if in cudpm, add 3
    # any other lower case add 2
    # any upper case, add 1 
    # any non letters except comma period and space, substract -10 

    score = 0
    for letter in text:
        if chr(letter).lower() in set('eariotnsl'): score += 4
        elif chr(letter).lower() in set('cudpm'): score += 3
        elif ord('a') <= letter <= ord('z'): score += 2
        elif ord('A') <= letter <= ord('Z'): score += 1
        elif chr(letter) not in set(' ,.'): score -= 10
    return score


with open('resources/cipher1.txt') as f:
    text = [int(x) for x in f.read().split(",")]
    


# get the key that produces the maximum text scoring for each combination
# we are trying with the first 20 characters only 

x = range(ord('a') , ord('z') + 1)
key = max( (p for p in itertools.product(x, repeat=3)) , key = lambda key :  score_string(decrypt(text[0:20], key)) )
print(sum(decrypt(text, key)))