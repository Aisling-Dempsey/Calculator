"""
calculator.py

Using our arithmetic.py file from Exercise02, create the
calculator program yourself in this file.
"""

from arithmetic import *


# Your code goes here


def tokenizing(user_input):
    """tokenizes user input"""

    input_list = user_input.split(" ")
    return input_list

# for testing!
#print tokenizing('+ 2 2')
print "Enter mathematical operation in prefix notation:"
while True:
    user_input = raw_input("> ")
    user_list = tokenizing(user_input)
    operator = user_list[0]
    num1 = user_list[1]
    if len(user_list) == 3:
        num2 = user_list[2]    




    #operator, num1, num2 = tokenizing(user_input)
    #for testing
    #print operator, num1, num2
    
    if operator == '+':
        print int(num1) + int(num2)
    
    elif operator == '-':
        print int(num1) - int(num2)
    
    elif operator == '*':
        print int(num1) * int(num2)
    
    elif operator == '/':
        print float(num1) / float(num2)
    
    elif operator == 'square':
        print int(num1) ** 2
    
    elif operator == 'cube':
        print int(num1) ** 3
    
    elif operator == 'pow':
        print int(num1) ** int(num2)
    
    elif operator == 'mod':
        print int(num1) % int(num2)    
    
    elif operator == "q":
        print "Good bye!"
        break

    else:
        print "That's not a valid input. Try again."




