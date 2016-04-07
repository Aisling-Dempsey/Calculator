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
    #assigns 'operator' from user_list
    operator = user_list[0]
    # #assigns 'num1' from user_list WHERE APPLICABLE
    # if len(user_list) >= 2: 
    #     num1 = user_list[1]
    # #assigns 'num2' from user_list WHERE APPLICABLE
    # if len(user_list) == 3:
    #     num2 = user_list[2]    
    
    #These are the mathematical operations
    if operator == '+':
        total = int(user_list[1])
        for num in user_list[2:]:
            if num[0] == '-':
                num = num[1:]
            else:
                pass
            if num.isdigit():
                total += int(num)
            else:
                print "That's not a valid input. Try again."
            # else:
            #     if num.isdigit():
            #         total += int(num)
            #     else:
            #         print "That's not a valid input. Try again."
        print total
    
    elif operator == '-':
        total = int(user_list[1])
        for num in user_list[2:]:
            if num.isdigit():
                total -= int(num)
            else:
                print "That's not a valid input. Try again."
        print total
    
    elif operator == '*':
        total = int(user_list[1])
        for num in user_list[2:]:
            if num.isdigit():
                total *= int(num)
            else:
                print "That's not a valid input. Try again."
        print total
    
    elif operator == '/':
        total = float(user_list[1])
        for num in user_list[2:]:
            if num.isdigit():
                total /= float(num)
            else:
                print "That's not a valid input. Try again."
        print total
    
    elif operator == 'square':
        num1 = user_list[1]
        if len(user_list) > 2 or not num.isdigit():
            print "That's not a valid input. Try again."
        else:
            print float(num1) ** 2

    
    elif operator == 'cube':
        num1 = user_list[1]
        if len(user_list) > 2 or not num.isdigit():
            print "That's not a valid input. Try again."
        else:
            print float(num1) ** 3
    
    elif operator == 'pow':
        total = float(user_list[1])
        for num in user_list[2:]:
            if num.isdigit():
                total = total ** float(num)
            else:
                print "That's not a valid input. Try again."
        print total
    
    elif operator == 'mod':
        total = int(user_list[1])
        for num in user_list[2:]:
            if num.isdigit():
                total = total % int(num)
            else:
                print "That's not a valid input. Try again."
        print total    
    
    #Allows user to quit
    elif operator == "q":
        print "Goodbye!"
        break
    
    #Catches incorrect inputs
    else:
        print "That's not a valid input. Try again."


#add try/except for errors for strings



