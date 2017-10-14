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



def eval_postfix(equation):
    stack = Stack()
    for charac in equation:
        if charac.isdigit():
            stack.push(charac)
        elif charac in ["+" , "-" , "/" , "*" , "^"]:
            if stack.size() >= 2:
                op1 = stack.pop()
                op2 = stack.pop()
                res = op2 + charac + op1
                res = eval(res)
                stack.push(str(res))
            else:
                return -1
    print("Answer is : %s"%stack.pop())

if __name__ == "__main__":
    eval_postfix("3+2")
