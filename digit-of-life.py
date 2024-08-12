'''
TZVM163 Cisco: Python programming (OpenEDG)
2.5.1.9 LAB: The Digit of Life
Student Name: Caroline Lau Campbell
'''

'''
Some say that the Digit of Life is a digit evaluated using somebody's 
birthday. It's simple - you just need to sum all the digits of the date. 
If the result contains more than one digit, you have to repeat the addition 
until you get exactly one digit. For example:

1 January 2017 = 2017 01 01
2 + 0 + 1 + 7 + 0 + 1 + 0 + 1 = 12
1 + 2 = 3
3 is the digit we searched for and found.

Your task is to write a program which:
- asks the user her/his birthday (in the format YYYYMMDD, or YYYYDDMM, or 
MMDDYYYY - actually, the order of the digits doesn't matter)
- outputs the Digit of Life for the date.

Test your code using the data we've provided.
'''

birthday = input('Enter your birthdate as YYYYMMDD: ')

def digit_of_life(birthday):
    digits = ''
    # Ensure only working with digits in case of typos
    for char in birthday:
        if char.isdigit():
            digits += char # str 'digits' only has digits concantenated
    digits = list(digits) # convert str to list
    
    while len(digits)>1:
        tally = 0
        for i in digits:
            tally += int(i)
        digits = list(str(tally)) # convert int to str then list
    
    return digits[0] # first and only value in list
    
print(f'Digit of Life is {digit_of_life(birthday)}.')

'''
#############
# Test data #
#############
19991229
output = 6

20000101
output = 4
'''
