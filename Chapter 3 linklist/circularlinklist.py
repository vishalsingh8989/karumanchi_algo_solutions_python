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
        lenght = len(self)
        if self._tail is None:
            self._tail = Node(data, None)
            self._tail.setNext(self._tail)
        else:
            temp = self._tail if position == 0 else self._tail.getNext()
            currentPosition = 0
            while temp is not self._tail and currentPosition<position - 1:
                currentPosition+=1
                temp = temp.getNext()
            if temp is None:
                raise Exception("List len is less than position ")
            else:
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
        lenght = len(self)
        if self._tail is None:
            print("List is empty")
            return 
        elif self._tail == self._tail.getNext():
            print("last element deleted")
            self._tail = None
        else:
            temp = self._tail if position == 0 else self._tail.getNext()
            currentPosition = 0 
            while temp is not self._tail and currentPosition<position - 1:
                currentPosition+=1
                temp = temp.getNext()
            if temp is None:
                raise Exception("List len is less than position")
            else:
                nextnode = temp.getNext()
                if position == 0:
                    self._tail.setNext(self._tail.getNext().getNext())
                else:
                    #pass
                    temp.setNext(nextnode.getNext())
                if position == lenght - 1:
                    print("last element deleted")
                    self._tail = temp

    def printlist(self):
        if self._tail is None:
            print("list is empty")
        elif self._tail.getNext()  == self._tail:
            print(self._tail.getData())
        else:
            print("***********************")
            temp = self._tail.getNext()
            while temp != self._tail:
                sys.stdout.write("%d "%(temp.getData()))
                #sys.stdout.write("%d, %s"%(temp.getData(), temp))
                temp = temp.getNext()
                sys.stdout.write(" --> ")
            sys.stdout.write("%d"%(temp.getData()))
        print("")            
if __name__ == "__main__":
    cl = CircularList()
    cl.insertAtPosition(0, 0)
    cl.insertAtPosition(10, 0)
    cl.insertAtPosition(20, 0)
    cl.insertAtPosition(30, 0)
    cl.printlist()
    
    cl.insertAtPosition(40, 0)
    cl.insertAtPosition(15,4)
    cl.insertAtPosition(-10, 6)
    length = len(cl)
    cl.insertAtPosition(-20, length )
    cl.insertAtPosition(-30, 8)
    
    cl.insertAtBegin(50)
    cl.insertAtEnd(-40)
    
    cl.printlist()
    print("Delete test %d"%len(cl) )
    cl.deleteAtPosition(0)
    cl.printlist()
    print("delete 2th element")
    cl.deleteAtPosition(2)
    cl.printlist()
    print("delete 8th element")
    cl.deleteAtPosition(8)
    cl.printlist()

