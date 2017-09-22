#!/usr/bin/python
__author__ = "Vishal Jasrotia. Stony Brook University"
__copyright__ = ""
__license__ = "GPL"
__version__ = "1.0"
__maintainer__ = "Vishal Jasrotia"
__email__ = "jasrotia.vishal@stonybrook.edu"
__status__ = ""

import os

class Node(object):

        def validate(f):
            def inner(*args, **kwargs):
                if isinstance(args[1], Node)  or args[1] is None:
                    f(args, kwargs)
                else:
                    raise Exception("next and previous node should be object of class Node or None")
            return inner


        def __new__(cls, data, nextNode, prevNode):
           if (isinstance(nextNode, Node) or nextNode is None) and (isinstance(prevNode, Node) or prevNode is None):
               return super(Node, cls).__new__(cls, data, nextNode, prevNode)
           else:
               raise Exception("next node should be object of class Node or None")

        def __init__(self, data, nextNode, prevNode):
            self._data = data
            self._nextNode = nextNode
            self._prev = prevNode

        @validate
        def setNext(self, nextNode):
            self._nextNode = nextNode

        @validate
        def setPrev(self, prevNode):
             self._prevNode = prevNode

        def getData(self):
            return self._data

        def setData(self, data):
            self._data = data

        def getNext(self):
            return self._nextNode

        def getPrev(self):
            return self._prevNode

node = Node(10, None, None)
print(node.getData())
