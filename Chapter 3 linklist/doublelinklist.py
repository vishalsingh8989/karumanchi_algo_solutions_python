#!/usr/bin/python
__author__ = "Vishal Jasrotia. Stony Brook University"
__copyright__ = ""
__license__ = "GPL"
__version__ = "1.0"
__maintainer__ = "Vishal Jasrotia"
__email__ = "jasrotia.vishal@stonybrook.edu"
__status__ = ""

import os, sys

class Node(object):

        def validate(f):
            def inner(*args, **kwargs):
                if isinstance(args[1], Node)  or args[1] is None:
                    f(*args, **kwargs)
                else:
                    raise Exception("next and previous node should be object of class Node or None")
            return inner


        def __new__(cls, data, nextNode, prevNode):
           if (isinstance(nextNode, Node) or nextNode is None) and (isinstance(prevNode, Node) or prevNode is None):
               return super(Node, cls).__new__(cls, data, nextNode, prevNode)

           else:
               raise Exception("next node should be object of class Node or None")

        def __init__(self, data, nextNode, prevNode):
            print("__init__ %s ( %d, %s , %s)"%(self,data, nextNode, prevNode))
            self._data = data
            self._nextNode = nextNode
            self._prevNode = prevNode

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


class DoubleLinklist:

    def __init__(self):
        self._head = None
        self._tail = None

    def __len__(self):
        temp = self._head
        count = 0
        while temp is not None:
            count+=1
            temp = temp.getNext()
        return count

    def insertAtBegin(self, data):
        if self._head is None:
            self._head = Node(data, None, None)
            self._tail = self._head
        else:
            tempnode = Node(data, self._head, None)
            self._head.setPrev(tempnode)
            self._head = tempnode


    def insertAtEnd(self, data):
        if self._tail is None:
            self._tail = Node(data, None, None)
            self._head = self._tail
        else:
            tempnode = Node(data, None, self._tail)
            self._tail.setNext(tempnode)
            self._tail = tempnode

    def insertAtPosition(self, data, position):
        if self._head is None:
            self.insertAtBegin(data)
        else:
            currentPosition = 0
            temp = self._head
            while temp is not None and currentPosition < position:
                temp = temp.getNext()
                currentPosition+=1
            if temp is None:
                raise Exception("List len is less than position")
            else:
                newNode = Node(data, temp, temp.getPrev())
                newNode.getPrev().setNext(newNode)
                temp.setPrev(newNode)


    def deleteFromPosition(self, position):
        if self._head is None or self._tail is None:
            print("list is empty")
        elif position == 0 :
            temp = self._head
            self._head = self._head.getNext()
            if self._head is None:
                self._tail = None
            else:
                self._head.setPrev(None)
            del temp
        elif position == len(self):
            temp = self._tail
            self._tail = self._tail.getPrev()
            if self._tail is not None:
                self._tail.setNext(None)
            else:
                self._head = None
        else:
            currentPosition = 0
            temp = self._head
            while temp is not None and currentPosition < position  :
                currentPosition+=1
                temp = temp.getNext()
            if temp is None:
                raise Exception("List len is less than position.")
            else:
                temp.getPrev().setNext(temp.getNext())
                temp.getNext().setPrev(temp.getPrev())
                del temp

    def deleteHead(self):
        self.deleteFromPosition(0)
    def deleteTail(self):
        self.deleteFromPosition(len(self))

    def printFromStart(self):
        """print list element from start.
        """
        if self._head is None:
            print("List is empty")
            return
        temphead = self._head
            
        while temphead is not None:
            sys.stdout.write("%d"%temphead.getData())
            temphead = temphead.getNext()
            if temphead is not None:
                sys.stdout.write(" -> ")
        print("")

    def printFromEnd(self):
        if self._tail is None:
            print("List is empty")
            return
        temptail = self._tail
        while temptail is not None:
            sys.stdout.write("%d"%temptail.getData())
            temptail = temptail.getPrev()
            if temptail is not None:
                sys.stdout.write(" -> ")
        print("")

if __name__ == "__main__":
    print("start")
    dlist  = DoubleLinklist()
    dlist.insertAtBegin(10)
    dlist.insertAtBegin(20)
    dlist.insertAtEnd(30)
    dlist.insertAtBegin(40)
    dlist.insertAtEnd(0)
    dlist.printFromStart()
    dlist.printFromEnd()
    dlist.deleteFromPosition(5)
    dlist.printFromStart()
    dlist.printFromEnd()
    dlist.deleteFromPosition(0)
    dlist.printFromStart()
    dlist.printFromEnd()

    dlist.deleteFromPosition(0)
    dlist.printFromStart()
    dlist.printFromEnd()
    dlist.deleteFromPosition(0)
    dlist.printFromStart()
    dlist.printFromEnd()
    dlist.deleteFromPosition(0)
    dlist.printFromStart()
    dlist.printFromEnd()
    
    dlist.insertAtBegin(10)
    dlist.insertAtEnd(20)
    dlist.insertAtBegin(0)
    dlist.insertAtEnd(30)
    dlist.insertAtEnd(40)
    dlist.insertAtEnd(50)

    dlist.printFromStart()
    dlist.printFromEnd()
    print("Delete from postion test")
    dlist.deleteFromPosition(1)
    dlist.printFromStart()
    dlist.printFromEnd()

    print("Delete head tail test")
    dlist.deleteHead()
    dlist.deleteTail()
    dlist.printFromStart()
    dlist.printFromEnd()
    print("Insert At position test")
    dlist.insertAtPosition(70,2 )
    dlist.printFromStart()
    dlist.printFromEnd()

    print("bye bye")
