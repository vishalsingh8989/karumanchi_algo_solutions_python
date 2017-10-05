#!/usr/bin/python
__author__ = "Vishal Jasrotia. Stony Brook University"
__copyright__ = ""
__license__ = "GPL"
__version__ = "1.0"
__maintainer__ = "Vishal Jasrotia"
__email__ = "jasrotia.vishal@stonybrook.edu"
__status__ = ""
__problem__ = 1

import sys
from stacks import *


open_bracket = "{[("
close_bracket = "}])"
bracket = open_bracket + close_bracket
priority = {'+':1, '-':1, '*':2, '/':2, '^':3}

def isgreater(val1, val2):
    try:
        a = priority.get(val1)
        b = priority.get(val2)
        if a >= b:
            return True
        else:
            return False
    except:
        return False



def infixToPostfix(equation = ""):
    stack = Stack()
    for charac in equation:
        #stack.printstack()
        if charac.isalpha():
            sys.stdout.write("%s"%charac)
        elif charac == "(":
            stack.push(charac)
        elif charac == ")":
            while stack.size() !=0 and stack.peek() != '(':
                top = stack.pop()
                sys.stdout.write("%s"%top)
            if not stack.size() == 0 and stack.peek() != '(':
                return -1
            else:
                stack.pop()
        else:
            while stack.size() !=0 and isgreater(stack.peek(), charac):
                sys.stdout.write("%s"%stack.pop())
            stack.push(charac)
    

    while stack.size()!=0:
        sys.stdout.write("%s"%stack.pop())

    print("")


if __name__ == "__main__":
    exp = "a+b*(c^d-e)^(f+g*h)-i"
    infixToPostfix(exp)

