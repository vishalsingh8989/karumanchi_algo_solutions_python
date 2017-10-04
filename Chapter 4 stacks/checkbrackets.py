#!/usr/bin/python
__author__ = "Vishal Jasrotia. Stony Brook University"
__copyright__ = ""
__license__ = "GPL"
__version__ = "1.0"
__maintainer__ = "Vishal Jasrotia"
__email__ = "jasrotia.vishal@stonybrook.edu"
__status__ = ""

import sys
from stacks import *


open_bracket = "{[("
close_bracket = "}])"

match = {"(":")" , "{":"}", "[":"]"}

bracket = open_bracket + close_bracket
def validateEquation(equation ="" ):
    stack = Stack()
    for charac in equation:
        if charac in bracket:
            if charac in open_bracket:
                stack.push(charac)
            if charac in close_bracket:
                if stack.size() == 0:
                    return "invalid"
                else:
                    top = stack.pop()
                    if match[top] != charac:
                        return "invalid"

    return "valid"


equation = "(a+b)"
res = validateEquation(equation)
print("%s is %s equation"%(equation, res))

equation = "(a+b)+(c+d))"
res = validateEquation(equation)
print("%s is %s equation"%(equation, res))


equation = "({[a+b]})"
res = validateEquation(equation)
print("%s is %s equation"%(equation, res))


equation = "(a+b)}"
res = validateEquation(equation)
print("%s is %s equation"%(equation, res))






