'''
TZVM163 Cisco: Python programming (OpenEDG)
2.4.1.6 LAB: A LED Display
Student Name: Caroline Lau Campbell
'''

'''
Your task is to write a program which is able to simulate the work of 
a seven-display device, although you're going to use single LEDs 
instead of segments.

Each digit is constructed from 13 LEDs (some lit, some dark, of course) 
- that's how we imagine it:

  # ### ### # # ### ### ### ### ### ### 
  #   #   # # # #   #     # # # # # # # 
  # ### ### ### ### ###   # ### ### # # 
  # #     #   #   # # #   # # #   # # # 
  # ### ###   # ### ###   # ### ### ###

Note: the number 8 shows all the LED lights on.

Your code has to display any non-negative integer number entered by the user.
'''

lights={
    '0':['###','# #','# #','# #','###'],
    '1':['  #','  #','  #','  #','  #'],
    '2':['###','  #','###','#  ','###'],
    '3':['###','  #','###','  #','###'],
    '4':['# #','# #','###','  #','  #'],
    '5':['###','#  ','###','  #','###'],
    '6':['###','#  ','###','# #','###'],
    '7':['###','  #','  #','  #','  #'],
    '8':['###','# #','###','# #','###'],
    '9':['###','# #','###','  #','###']
}

def seven_segment_display(input_number):
    led_rows=['','','','','']
    for digit_key in input_number:
        for i in range(5):
            led_rows[i]+=lights[digit_key][i]+' '
    for row in led_rows:
        print(row)

#test_input='9081726354'    
#seven_segment_display(test_input)

try:
    user_input=input('Enter a non-negative integer: ')
    seven_segment_display(user_input)
except:
    print('Sorry; non-negative integers only.')
