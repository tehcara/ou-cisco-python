'''
TZVM163 Cisco: Python programming (OpenEDG)
2.5.1.6 LAB: Improving the Caesar cipher
Student Name: Caroline Lau Campbell
'''

'''
You are already familiar with the Caesar cipher, and this is why we 
want you to improve the code we showed you recently.

The original Caesar cipher shifts each character by one: a becomes b, 
z becomes a, and so on. Let's make it a bit harder, and allow the 
shifted value to come from the range 1..25 inclusive.

Moreover, let the code preserve the letters' case (lower-case letters 
will remain lower-case) and all non-alphabetical characters should 
remain untouched.

Your task is to write a program which:

- asks the user for one line of text to encrypt;
- asks the user for a shift value (an integer number from the range 
1..25 - note: you should force the user to enter a valid shift value 
(don't give up and don't let bad data fool you!)
- prints out the encoded text.

Test your code using the data we've provided.
'''

def get_valid_shift():
    while True:
        try:
            shift = int(input('Enter a shift value (1-25): '))
            if 1 <= shift <= 25:
                return shift
            else:
                print('Please enter a number between 1 and 25.')
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

def get_user_text():
    while True:
        try:
            user_text = input('Enter a message to encrypt: ')
            if user_text.strip() != '':
                return user_text
            else:
                print('Please enter at least one character.')
        except ValueError:
            print('Invalid input. Please enter a valid string.')
 
def caesar_cipher(text, shift):
    cipher = ""
    for char in text:
        if char.isalpha():
            shift_value = shift % 26
            if char.islower():
                new_char = chr((ord(char) - ord('a') + shift_value) % 26 + ord('a'))
            else:
                new_char = chr((ord(char) - ord('A') + shift_value) % 26 + ord('A'))
            cipher += new_char
        else:
            cipher += char
    return cipher            

shift = get_valid_shift()
text = get_user_text()
msg = caesar_cipher(text, shift)
print('Encrypted text:', msg)

'''
#############
# Test data #
#############
text = abcxyzABCxyz 123
shift = 2
msg = cdezabCDEzab 123

text = The die is cast
shift = 25
msg = Sgd chd hr bzrs

####################
# OG caesar cipher #
####################
text = input("Enter your message: ")
cipher = ''
for char in text:
    if not char.isalpha():
        continue
    char = char.upper()
    code = ord(char) + 1
    if code > ord('Z'):
        code = ord('A')
    cipher += chr(code)
print(cipher)
'''
