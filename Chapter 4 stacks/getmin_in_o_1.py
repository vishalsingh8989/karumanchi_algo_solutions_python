#!/usr/bin/python
__author__ = "Vishal Jasrotia. Stony Brook University"
__copyright__ = ""
__license__ = "GPL"
__version__ = "1.0"
__maintainer__ = "Vishal Jasrotia"
__email__ = "jasrotia.vishal@stonybrook.edu"
__status__ = ""
__problem__ = 6
"""
get minimun element in stack in O(1) time
 
"""

import sys
from stacks import *



class AdvancedStack(Stack):
    def __init__(self):
        Stack.__init__(self)
        self.min_stack = []
        self._current_min = 100000
    def push(self,data):
        Stack.push(self,data)
        if data < self._current_min:
            self.min_stack.insert(0, data)
            self._current_min = data
        else:
            self.min_stack.insert(0, self._current_min)
    def printstack(self):
        Stack.printstack(self)
        print("MIN STACK FOR ABOVE STACK IS:")
        print("+----------------+")
        for x in self.min_stack:
            print("|       %d       |"%x)
            print("+----------------+")

    def pop(self):
        Stack.pop(self)
        self.min_stack.pop(0)
    
    def getmin(self):
        return self.min_stack[0]



