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
            if isinstance(args[0], Node) or args[0] is None:
                f(*args, **kwargs)
            else:
                raise Exception("init_error")
        return inner

    def __new__(cls, data, nextNode):
        if isinstance(nextNode, Node) or nextNode is None:
            return super(Node, cls).__new__(cls, data,nextNode)
        else:
            raise Exception("init error")

    def __init__(self, data, nextNode):
        self._data=data
        self._nexNode = nextNode

    @validate
    def setNext(self, nextNode):
        self._nextNode = nextNode

    def getNext(self):
        return self._nextNode

    def getData(self):
        return self._data

class Stack:
    def __init__(self):
        self._top = None
    def push(self, data):
        if self._top is None:
            self._top  = Node(data, None)
        else:
            newNode = Node(data, self._top)
            self._top = newNode
    def pop(self):
        if self._top is None:
            raise Exception("Stack is empty")
        else:
            temp = self._top
            self._top = self._top.getNext()
            return temp.getData()
    def peek(self):
        if self._top is None:
            pass
        else:
            te
