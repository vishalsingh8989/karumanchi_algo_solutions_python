#!/usr/bin/python
from __future__ import print_function
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
def isLinkListSorted(head):
    
    while head.next is not None:
        
        if head.data >  head.next.data:
            return False
        head = head.next
        
    return True

def printlistrev(tail):
    print("\nLink list :" ,end = " : ")
    start = tail
    while tail is not None and tail.prev is not start:
        print(tail, end = " -> ")
        tail = tail.prev
    if tail is not None:
        print

def printlist(head):
    print("\nLink list :" ,end = " : ")
    start = head
    last = head
    while head is not None and head.next is not start:
        print(head, end = " -> ")
        last = head
        head = head.next
        
    if head is not None:
        print(str(head.data) + " -> start", end = " -> ")
    print()
    return last   
       
class DoubleNode:
    def __init__(self, data, prev, next):
        self.data = data
        self.next = next
        self.prev = prev
     
    def __repr__(self):
        if self.next is None:
            next =  "next(None)"
        else:
            next = "next(" +str(self.next.data)+ ")"
             
        if self.prev is None:
            prev = "prev(None)"
        else:
            prev = "prev(" +str(self.prev.data)+ ")"
            
        rpr = "[ " + prev + ", " +str(self.data) + ", " + next + " ]" 
        return rpr
     
class SimpleNode:
    def __init__(self, data, next):
        self.data = data
        self.next = next
    
    def __repr__(self):
        if self.next is None:
            rpr = " [ "+str(self.data) + ", next(None) ] "
        else:
            rpr = " [ "+str(self.data) + ", next("+str(self.next.data)+") ] "
        return rpr
        
class Node(object):
    """ single link list node
    """
    def validate(f):
        def wrapper(*args, **kwargs):
            if not isinstance(args[1], Node) and args[1] is not None:
                raise Exception("Second argument should be either None or obj of class  Node")
            else:
                f(*args,**kwargs)
        return wrapper

    def __new__(cls, data, nextNode):
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

    def setData(self, data):
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
            raise Exception("KeyError: key should integer.")
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

    def insertAtPosition(self, data, position):
        if self._head is None:
            self._head= Node(data, None)
        else:
            count = 0
            temphead = self._head
            while temphead.getNext() is not None and count < position - 1:
                temphead = temphead.getNext()
                count+=1
            if position == 0 : #newNode is now head, if added at 0 position
                newNode = Node(data, temphead)
                self._head = newNode
            else:
                newNode = Node(data, temphead.getNext())
                temphead.setNext(newNode)

    def deleteHead(self):
        if self._head is None:
            print("list is empty")
        else:
            temphead = self._head
            if temphead is not None:
                self._head = self._head.getNext()
                del temphead
            else:
                self._head = None
    def deleteTail(self):
        if self._head is None:
           print("list is empty")
        else:
            temphead = self._head
            temppre = None
            while temphead is not None and temphead.getNext() is not None:
                temppre = temphead
                temphead = temphead.getNext()
            if temppre is not None: # where list had only one element
                temppre.setNext(None)
            else:  #list had only one element
                self._head = None
            del temphead
            del temppre

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


    def getHead(self):
        return self._head

if __name__ == "__main__":
    linklist = LinkList()
    linklist.insertAtBegin(20)
    linklist.insertAtBegin(30)
    linklist.insertAtBegin(40)
    linklist.insertAtBegin(50)
    linklist.printLinklist()
