"""
calculator.py

Using our arithmetic.py file from Exercise02, create the
calculator program yourself in this file.
"""

from arithmetic import *


def tokenizing(user_input):
    """tokenizes user input"""
    user_input = user_input.rstrip()
    input_list = user_input.split(" ")
    return input_list


print "Enter mathematical operation in prefix notation:"
while True:
    user_input = raw_input("> ")
    user_list = tokenizing(user_input)
    #assigns 'operator' from user_list
    operator = user_list[0] 
    
    #These are the mathematical operations

    # Addition
    if operator == '+':
        total = user_list[1]
        try: 
            for num in user_list[2:]:
                total = int(total)
                num = int(num)
                total += int(num)
            
            print total
        
        except ValueError:
            print "That's not a valid input. Try again."
            print "This is the problem!"
            
    # Subtraction
    elif operator == '-':
        total = user_list[1]
        try: 
            for num in user_list[2:]:
                total = int(total)
                num = int(num)
                total -= int(num)
            
            print total
        
        except ValueError:
            print "That's not a valid input. Try again."
    
    # Multiplication
    elif operator == '*':
        total = user_list[1]
        try: 
            for num in user_list[2:]:
                total = int(total)
                num = int(num)
                total *= int(num)
            
            print total
        
        except ValueError:
            print "That's not a valid input. Try again."

    # Division
    elif operator == '/':
        total = user_list[1]
        try: 
            for num in user_list[2:]:
                total = float(total)
                num = float(num)
                total /= float(num)
            
            print total
        
        except ValueError:
            print "That's not a valid input. Try again."
    
    # 2nd Power
    elif operator == 'square':
        total = user_list[1]
        if len(user_list) == 2:
            try: 
                num = user_list[1]
                print float(num) ** 2
                   
            except ValueError:
                print "That's not a valid input. Try again."            
        else: 
            print "That's not a valid input. Try again."            

    # 3rd Power
    elif operator == 'cube':
        total = user_list[1]
        if len(user_list) == 2:
            try: 
                num = user_list[1]
                print float(num) ** 3
                   
            except ValueError:
                print "That's not a valid input. Try again."            
        else: 
            print "That's not a valid input. Try again."     
    
    # Nth Power
    elif operator == 'pow':  
        total = user_list[1]
        try: 
            for num in user_list[2:]:
                total = float(total)
                num = float(num)
                total = total ** float(num)
            
            print total
        
        except ValueError:
            print "That's not a valid input. Try again."

    # Modulo
    elif operator == 'mod':
        total = user_list[1]
        try: 
            for num in user_list[2:]:
                total = int(total)
                num = int(num)
                total = total % int(num)
            
            print total
        
        except ValueError:
            print "That's not a valid input. Try again."
    
    #Allows user to quit
    elif operator == "q":
        print "Goodbye!"
        break
    
    #Catches incorrect inputs
    else:
        print "That's not a valid input. Try again."
