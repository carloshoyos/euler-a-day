"""
Project Euler Problem 17
========================

If the numbers 1 to 5 are written out in words: one, two, three, four,
five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written
out in words, how many letters would be used?

NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and
forty-two) contains 23 letters and 115 (one hundred and fifteen) contains
20 letters. The use of "and" when writing out numbers is in compliance
with British usage.
"""

#  Not a hard problem but oh boy  a lot of prep coding :(



# two approaches:   
# plan 1 - calculate only what's needed:  

# plan 2 - general purpose function number_to_english, evaluate for each number 

digits = {0: '', 1:'one', 2:'two', 3:'three', 4:'four', 5:'five', 6:'six', 7:'seven', 8:'eight', 9:'nine', 10:'ten', 
            11:'eleven', 12:'twelve', 13:'thirteen', 14:'fourteen', 15:'fifteen',  16:"sixteen", 17:"seventeen", 18:"eighteen", 19:"nineteen",
            20:'twenty', 30:"thirty", 40:"forty", 50:"fifty", 60:"sixty", 70:"seventy", 80:"eighty", 90:"ninety"}


units_count = sum(len(digits[i]) for i in range(1,10))

#tens_count = sum()


# plan 1 - calculate only what's needed and reuse 
# 1) calculate count 1 to 99  (tens_count)
#    1a) manually count letters of one to 9 (units_count)    Same for 10 to 19.  (teens_count)
#    1b) for 2x to 9x...  10* ('twenty') +  (units_count)
# 2) for the 1xx digits the count is 100 x ('onehundred') + 99 x 'and' +  tens_count
# 3) repeat for the 2xx to 9xx digits
# 4) add one thousand  (11)

def count_letters_numbers_to_1000():
    units_count = sum(len(digits[x]) for x in range(1,10) )     # 1 to 9
    teens_count = sum(len(digits[x]) for x in range(10,20) )    # 10 to 19
    tens_count = units_count + teens_count + sum( (len(digits[x]) * 10 + units_count) for x in range(20,100,10) )
    hund_count = sum( (len(digits[x]+'hundred')*100 + len('and')*99 + tens_count ) for x in range(1,10) )
    return tens_count + hund_count + len('onethousand')


# plan 2 - general function 
def number_to_english(number):
    if number <= 20:
        return digits[number]
    elif number < 100:
        return digits[(number // 10) * 10] + digits[number % 10]
    elif number <1000: 
        return digits[(number // 100)] + 'hundred' + ( "and"+number_to_english(number%100) if number%100 != 0 else "" )
    elif number <1000000: 
        return digits[(number // 1000)] + 'thousand' + (number_to_english(number%1000) if number%1000 != 0 else "" )


#plan 1
print(count_letters_numbers_to_1000())

#plan2
#print( sum(len(number_to_english(i)) for i in range(1,1001))  )


