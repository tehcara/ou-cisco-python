'''
TZVM163 Cisco: Python programming (OpenEDG)
2.8.1.4 Reading ints safely
Student Name: Caroline Lau Campbell
'''

'''
Your task is to write a function able to input integer values and to check 
if they are within a specified range.

The function should:
- accept three arguments: a prompt, a low acceptable limit, and a high 
acceptable limit;
- if the user enters a string that is not an integer value, the function 
should emit the message Error: wrong input, and ask the user to input the 
value again;
- if the user enters a number which falls outside the specified range, the 
function should emit the message Error: the value is not within permitted 
range (min..max) and ask the user to input the value again;
- if the input value is valid, return it as a result.

Test your code using the data we've provided.
'''

def read_int(prompt, min, max):
    flag = True # flag the condition
    while flag:
        try:
            x = int(input(prompt)) # use prompt for user input prompt
            if x>=-10 and x<=10: # check range
                flag = False # flag conditions met
            else:
                print('Error: the value is not within permitted range (min..max)')
                continue # repeat loop if input outside range
        except ValueError: # catch non-int user input
            print('Error: wrong input')
    return x


v = read_int("Enter a number from -10 to 10: ", -10, 10)

print("The number is:", v)

'''
#############
# Test data #
#############
Enter a number from -10 to 10: 100
Error: the value is not within permitted range (-10..10)
Enter a number from -10 to 10: asd
Error: wrong input
Enter number from -10 to 10: 1
The number is: 1
'''
