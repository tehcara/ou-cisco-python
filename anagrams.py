'''
TZVM163 Cisco: Python programming (OpenEDG)
2.5.1.8 LAB: Anagrams
Student Name: Caroline Lau Campbell
'''

'''
An anagram is a new word formed by rearranging the letters of a word, 
using all the original letters exactly once. For example, the phrases 
"rail safety" and "fairy tales" are anagrams, while "I am" and "You are" 
are not.

Your task is to write a program which:
- asks the user for two separate texts;
- checks whether, the entered texts are anagrams and prints the result.

Note:
- assume that two empty strings are not anagrams;
- treat upper- and lower-case letters as equal;
- spaces are not taken into account during the check - treat them as non-existent

Test your code using the data we've provided.
'''

string1 = input('Enter string 1: ')
string2 = input('Enter string 2: ')

def clean_text(text):
    cleaned_text = ''
    for char in text:
        # Remove spaces and convert to same typecase
        if char != ' ':
            cleaned_text += char.lower()
    return cleaned_text

def is_anagram(str1, str2):
    clean_str1 = clean_text(str1)
    clean_str2 = clean_text(str2)
    if len(str1) != len(str2):
        return False
    else:
        sorted_string1 = sorted(clean_str1)
        sorted_string2 = sorted(clean_str2)
        return sorted_string1 == sorted_string2

if is_anagram(string1, string2):
    print('Anagrams')
else:
    print('Not anagrams')
    
'''
#############
# Test data #
#############
Listen
Silent
output= Anagrams

modern
norman
output = Not anagrams
'''
