#!/usr/bin/python
__author__ = "Vishal Jasrotia. Stony Brook University"
__copyright__ = ""
__license__ = "GPL"
__version__ = "1.0"
__maintainer__ = "Vishal Jasrotia"
__email__ = "jasrotia.vishal@stonybrook.edu"
__status__ = ""


#imports start
import sys


#import end

class Node(object):
    """ link list node 
    """
    def validate(f):
        def wrapper(*args, **kwargs):
            if not isinstance(args[1], Node) and args[1] is not None:
                raise Exception("Second argument should be either None or obj of class  Node")
            else:
                f(*args,**kwargs)
        return wrapper
            
    def __new__(cls, data, nextNode):
        print("In __new__")
        if not isinstance(nextNode, Node) and nextNode is not None :
            raise Exception("Second argument should be either None or obj of class  Node")
        else:
            return super(Node, cls).__new__(cls, data, nextNode)

    def __init__(self, data, nextNode):
        """check  validity of nextNode in __new__. If not valid then dont init.
        """
        self._data     = data
        self._nextNode = nextNode
    
    @validate
    def setNext(self, nextNode):
        self._nextNode = nextNode

    def getNext(self):
        return self._nextNode

    def setData(self, _data):
        self._data = data

    def getData(self):
        return self._data


class LinkList:
    """
    """
    def __init__(self):
        self._head = None
        
    def __call__(self):
        print("__call__")

    def __str__(self):
        print("__str__")
    
    def __repr__(self):
        """ method to represent object of class Linklist example: linklist = LinkList()
        and then just print(linklist) will call __repr__ function
        """
        rpr = "["
        temphead = self._head
        while temphead is not None:
            rpr = rpr+ "%d"%(temphead.getData())
            temphead = temphead.getNext()
            if temphead is not None:
                rpr = rpr + ", "
        rpr = rpr + " ]"
        return rpr

    def __getitem__(self, key):
        if not isinstance(key, int):
            raise Exception("KeyError: key should in integer.")
        count = 0
        temphead = self._head
        while temphead is not None and count < key:
            temphead = temphead.getNext()
            count = count + 1
        if count != key :
            raise Exception("IndexError: index out of bound.")
        else:
            print(temphead.getData())
    def __len__(self):
        count  = 0
        temphead = self._head
        while temphead is not None:
            temphead = temphead.getNext()
            count +=1
        return count

    def insertAtBegin(self, data):
        node  = Node(data, self._head) # create new node which will be newh head poitiong to previuos head and return new node(new head)
        self._head = node

    def insertAtEnd(self, data):
        temphead = self._head
        while temphead is not None and temphead.getNext() is not None:
            temphead = temphead.getNext()
        tempNode = Node(data, None)
        temphead.setNext(tempNode)
        
    def deleteHead(self):
        temphead = self._head
        if temphead is not None:
            self._head = self._head.getNext()
            del temphead
    def deleteTail(self):
        temphead = self._head
        temppre = None
        while temphead is not None and temphead.getNext() is not None:
            temppre = temphead
            temphead = temphead.getNext()
        
        temppre.setNext(None)
        del temphead
    def deleteAtPosition(self, pos):
        """ delete at position. 
        @Known issue: No handling for pos is more than length of the list.2 pos is 0
        """
        temphead = self._head
        temppre=None
        count = 0
        while count < pos and temphead is not None and temphead.getNext() is not None:
            temppre = temphead
            temphead = temphead.getNext()
            count = count + 1
        temppre.setNext(temphead.getNext())
        del temphead

    def printLinklist(self):
        temphead = self._head
        sys.stdout.write("")
        while temphead is not None:
            sys.stdout.write("%d"%(temphead.getData()))
            temphead = temphead.getNext()
            if temphead is not None:
                sys.stdout.write(" -> ")
        sys.stdout.write("")
        print("")


if __name__ == "__main__":
    linklist = LinkList() 
    linklist.insertAtBegin(20)
    linklist.insertAtBegin(30)
    linklist.insertAtBegin(40)
    linklist.insertAtBegin(50)
    linklist.printLinklist()


