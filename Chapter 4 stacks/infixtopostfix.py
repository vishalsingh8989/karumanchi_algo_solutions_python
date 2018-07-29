#!/usr/bin/python
__author__ = "Vishal Jasrotia. Stony Brook University"
__copyright__ = ""
__license__ = "GPL"
__version__ = "1.0"
__maintainer__ = "Vishal Jasrotia"
__email__ = "jasrotia.vishal@stonybrook.edu"
__status__ = ""
__problem__ = 2

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
    st = Stack()
    res = ""
    
    for charac in equation:
        #print(charac)
        if charac.isalpha():
            res = res + charac
        elif charac == "(":
            st.push(charac)
        elif charac == ")":
            while st.size() != 0 and st.peek() != "(":
                res = res + st.pop()
            st.pop()
            
        else:
            while st.size() != 0 and isgreater(st.peek(), charac):
                res = res +st.pop()
            st.push(charac)
        
        
    while st.size() > 0 :
        res = res + st.pop()
    
    return res
            
                
            
    

    while stack.size()!=0:
        sys.stdout.write("%s"%stack.pop())

    print("")


if __name__ == "__main__":
    exp = "a+b*(c^d-e)^(f+g*h)-i"
    print(infixToPostfix(exp))

