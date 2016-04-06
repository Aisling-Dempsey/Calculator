"""
calculator.py

Using our arithmetic.py file from Exercise02, create the
calculator program yourself in this file.
"""

from arithmetic import *


# Your code goes here


def tokenizing(user_input):
    input_list = user_input.split(" ")
    return input_list

print tokenizing('+ 2 2')
