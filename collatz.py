"""
TZVM163 Cisco: Python programming (OpenEDG)
3.2.1.15 LAB: Collatz's hypothesis
Student Name: Caroline Lau Campbell
"""

"""
The steps for Collatz's hypothesis are described in the lab as:

  1. take any non-negative and non-zero integer number and name it c0;
  2. if it's even, evaluate a new c0 as c0 ÷ 2;
  3. otherwise, if it's odd, evaluate a new c0 as 3 × c0 + 1;
  4. if c0 ≠ 1, skip to point 2.
  
The hypothesis says that regardless of the initial value of c0, 
it will always evaluate to 1.

The program takes one natural number, executes the above steps,
counts the steps, and outputs all the intermediate values of c0
on its way to 1. If it is already 1, there are zero steps.
"""

c0 = int(input('Enter a non-negative, non-zero integer: ')) # user input

i = 0 # counter

while c0 != 1:
    if c0%2 == 0: # if c0 is even
        c0 = c0/2
    else: # if c0 is odd
        c0 = 3 * c0 +1
    i += 1 # increment counter
    print(int(c0)) # print intermediate int values of c0
    if c0 == 1:
        break # end steps if/when c0 is 1

print('steps = '+str(i))
