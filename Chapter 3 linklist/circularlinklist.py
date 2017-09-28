#!/usr/bin/python
__author__ = "Vishal Jasrotia. Stony Brook University"
__copyright__ = ""
__license__ = "GPL"
__version__ = "1.0"
__maintainer__ = "Vishal Jasrotia"
__email__ = "jasrotia.vishal@stonybrook.edu"
__status__ = ""

import os, sys,time

class Node(object):
    """Single Circular link list node
    """
    def validate(f):
        def inner(*args, **kwargs):
            if  isinstance(args[1], Node) or args[1] is None:
                f(*args, **kwargs)
            else:
                raise Exception("next Node should be None or instance of NOde class.")
        return inner

    def __new__(cls, data, nextNode):
            if isinstance(nextNode, Node) is Node or nextNode is None:
                return super(Node, cls).__new__(cls, data, nextNode)
            else:
                raise Exception("next Node should be None or instance of Node class")

    def __init__(self, data, nextNode):
        self._data = data
        self._nextNode = nextNode

    @validate
    def setNext(self,  nextNode):
        self._nextNode = nextNode

    def getNext(self):
        return self._nextNode

    def getData(self):
        return self._data

class CircularList:

    def __init__(self):
        self._tail = None

    def __len__(self):
        if self._tail is None:
            return 0
        elif self._tail.getNext() is None:
            return 1
        temp = self._tail.getNext()
        count = 1
        while temp is not self._tail and temp is not None:
            count+=1
            temp = temp.getNext()
        return count #count tail

    def insertAtPosition(self, data, position):
        print(len(self))
        lenght = len(self)
        if self._tail is None:
            self._tail = Node(data, None)
            self._tail.setNext(self._tail)
        else:
            print("tail %d"%self._tail.getData()) 
            temp = self._tail if position == 0 else self._tail.getNext()
            currentPosition = 0
            while temp is not self._tail and currentPosition<position - 1:
                currentPosition+=1
                temp = temp.getNext()
            if temp is None:
                raise Exception("List len is less than position ")
            else:
                print("insert %d after %d, %d"%(data,temp.getData(), currentPosition ))
                newnode = Node(data, None)
                newnode.setNext(temp.getNext())
                temp.setNext(newnode)
                if position == lenght : 
                    self._tail =newnode

    def insertAtBegin(self, data):
        self.insertAtPosition(data, 0)

    def insertAtEnd(self, data):
        self.insertAtPosition(data, len(self))


    def deleteAtPosition(self, position):
        if self._head is None:
            print("List is empty")
            return 
        elif self._head == self._tail:
            self._head = None
            self._tail = None
        else:
            currentPosition = 0 
            temp = self._head
            while temp is not None and currentPosition < position - 1:
                temp = temp.getNext()
                currentPosition+=1
            print("At %d"%temp.getData())
            if temp is None:
                raise Exception("List len is less than position.")
            else:
                if position == 0:
                    self._head = self._head.getNext()
                    self._tail.setNext(self._head)
                    del temp
                elif position == len(self)- 1:
                    print("in elif")
                    temp.setNext(self._head)
                    self._tail = temp
                else:
                    print("in else")
                    tempnext = temp.getNext()
                    temp.setNext(tempnext.getNext())
                    del tempnext


    def printlist(self):
        if self._tail is None:
            print("list is empty")
        elif self._tail.getNext()  == self._tail:
            print(self._tail.getData())
        else:
            print("***********************")
            print(self._tail.getData())
            temp = self._tail.getNext()
            while temp is not self._tail:
                sys.stdout.write("%d"%temp.getData())
                temp = temp.getNext()
                sys.stdout.write(" -> ")
            sys.stdout.write("%d"%temp.getData())
        print("")            
if __name__ == "__main__":
    cl = CircularList()
    cl.insertAtPosition(0, 0)
    cl.insertAtPosition(10, 0)
    cl.insertAtPosition(20, 0)
    cl.insertAtPosition(30, 0)
    cl.insertAtPosition(40, 0)
    cl.insertAtPosition(15,4)
    cl.insertAtPosition(-10, 6)
    lenght = len(cl)
    print("len of list %d"%lenght)
    cl.insertAtPosition(-20, lenght )
    #cl.insertAtPosition(-30, 9)
    
    #cl.insertAtBegin(50)
    #cl.insertAtEnd(-40)
    
    cl.printlist()
    print("Delete test %d"%len(cl) )
    cl.deleteAtPosition(0)
    cl.printlist()
    cl.deleteAtPosition(9)
    cl.printlist()
