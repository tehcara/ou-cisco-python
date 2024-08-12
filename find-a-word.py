'''
TZVM163 Cisco: Python programming (OpenEDG)
2.5.1.10 LAB: Find a word!
Student Name: Caroline Lau Campbell
'''

'''
Let's play a game. We will give you two strings: one being a word 
(e.g., "dog") and the second being a combination of any characters.

Your task is to write a program which answers the following question: 
are the characters comprising the first string hidden inside the 
second string?

For example:
- if the second string is given as "vcxzxduybfdsobywuefgas", the answer is yes;
- if the second string is "vcxzxdcybfdstbywuefsas", the answer is no (as 
there are neither the letters "d", "o", or "g", in this order)

Hints:
- you should use the two-argument variants of the pos() functions inside your code;
don't worry about case sensitivity.

Test your code using the data we've provided.
'''

def is_hidden(word, string):
    pos = 0 # position counter for str search
    for char in word:
        # If find char at x position then pos counter is 1 or more
        pos = string.find(char, pos) + 1
        if pos == 0: # If cannot find char then pos counter will be 0
            return False
    return True

# Long-winded tack-on that could easily go in main func
def speechify():
    global res
    res = ''
    if is_hidden(hidden_word, str_to_search):
        res = 'Yes'
    else:
        res = 'No'

hidden_word = input('Enter hidden word: ')
str_to_search = input('Enter any combination of characters: ')
speechify() # Need to turn output into expected Yes/No str

print(f'Was your word hidden in your string? {res}!')

'''
#############
# Test data #
#############
donor
Nabucodonosor
output = Yes

donut
Nabucodonosor
output = No
'''
