'''
TZVM163 Cisco: Python programming (OpenEDG)
2.5.1.7 LAB: Palindromes
Student Name: Caroline Lau Campbell
'''

'''
Do you know what a palindrome is?

It's a word which look the same when read forward and backward. For 
example, "kayak" is a palindrome, while "loyal" is not.

Your task is to write a program which:
- asks the user for some text;
- checks whether the entered text is a palindrome, and prints result.

Note:
- assume that an empty string isn't a palindrome;
- treat upper- and lower-case letters as equal;
- spaces are not taken into account during the check - treat them as non-existent;
- there are more than a few correct solutions - try to find more than one.

Test your code using the data we've provided.
'''

def is_palindrome_v1(text):
    # Remove spaces and convert to same typecase
    cleaned_text = ''.join(char.upper() for char in text if char.isalnum())
    # Check if the cleaned text is the same forwards and backwards
    return cleaned_text == cleaned_text[::-1]

def get_palindrome_v1():
    text = input('Enter some text: ')
    if text == '':
        print('An empty string isn\'t a palindrome.')
    else:
        if is_palindrome_v1(text):
            print('It\'s a palindrome.')
        else:
            print('It\'s not a palindrome.')
    
def clean_text_v2(text):
    cleaned_text = ''
    for char in text:
        # Remove spaces and convert to same typecase
        if char.isalnum():
            cleaned_text += char.lower()
    return cleaned_text

def is_palindrome_v2(text):
    cleaned_text = clean_text_v2(text)
    # Return bool for if cleaned text is the same forwards and backwards
    return cleaned_text == cleaned_text[::-1]

def get_palindrome_v2():
    text = input('Enter some text: ')
    if not text:
        print('An empty string isn\'t a palindrome.')
    else:
        if is_palindrome_v2(text):
            print('It\'s a palindrome.')
        else:
            print('It\'s not a palindrome.')

get_palindrome_v1()
get_palindrome_v2()

'''
#############
# Test data #
#############
input = Ten animals I slam in a net
output= It's a palindrome

input= Eleven animals I slam in a net
output = It's not a palindrome
'''
