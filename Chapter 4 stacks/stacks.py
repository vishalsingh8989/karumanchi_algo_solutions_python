#!/usr/bin/python
__author__ = "Vishal Jasrotia. Stony Brook University"
__copyright__ = ""
__license__ = "GPL"
__version__ = "1.0"
__maintainer__ = "Vishal Jasrotia"
__email__ = "jasrotia.vishal@stonybrook.edu"
__status__ = ""

import sys


class Node:
    def validate(f):
        def inner(*args, **kwargs):
            f(*args, **kwargs)

        return inner

    def __init__(self, data, nextNode):
        self._data=data
        self._nexNode = nextNode


class Stack:
    """implementation of stack using python builtin list. 
        Stack can be implemeted using above node class.
    """
    def __init__(self):
        self._stack = []

    def pop(self):
        if len(self._stack) == 0:
            raise Exception("Stack is empty")
        data = self._stack.pop(0)
        return data

    def push(self, data):
        self._stack.insert(0, data)
    
    def peek(self):
        return self._stack[0]

    def size(self):
        return  len(self._stack)

    def printstack(self):
        for x in self._stack:
            print("+----------------+")
            print("|       %s        |"%str(x))
        print("------------------")

if __name__ == "__main__":
    stack = Stack()
    print("psuh 6,5,4,3 and print stack")
    stack.push(6)
    stack.push(5)
    stack.push(4)
    stack.push(3)
    stack.printstack()
    print("Top is : %d"%stack.pop())
    print("print after pop")
    stack.printstack()
    print("Peek top : %d "%stack.pop())
    


