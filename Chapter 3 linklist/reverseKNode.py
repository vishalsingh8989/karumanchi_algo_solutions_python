#!/usr/bin/python
__author__ = "Vishal Jasrotia. Stony Brook University"
__copyright__ = ""
__license__ = "GPL"
__version__ = "1.0"
__maintainer__ = "Vishal Jasrotia"
__email__ = "jasrotia.vishal@stonybrook.edu"
__status__ = ""


#imports start
import sys, time
#import end

from linklist import *



def reverseKNode(head, k ): 

    current = head;
    nextnode = prevnode = None
    count = 0
    while current is not None and count <  k:
        nextnode = current.getNext()
        current.setNext(prevnode)
        prevnode = current
        current  = nextnode
        count += 1

    if nextnode is not None:
        temp = reverseKNode(nextnode, k)
        head.setNext(temp)
    return prevnode


    


if  __name__ == "__main__":
    ll = LinkList()
    ll.insertAtBegin(0)
    ll.insertAtBegin(1)
    ll.insertAtBegin(2)
    ll.insertAtBegin(3)
    ll.insertAtBegin(4)
    ll.insertAtBegin(5)
    ll.insertAtBegin(6)
    ll.insertAtBegin(7)
    ll.insertAtBegin(8)
    ll.insertAtBegin(9)
    ll.insertAtBegin(10)
    ll.insertAtBegin(11)
    ll.insertAtBegin(12)
    ll.insertAtBegin(13)
    ll.insertAtBegin(14)
    ll.insertAtBegin(15)
    ll.printLinklist()
    ll._head = reverseKNode(ll.getHead(), 3)
    ll.printLinklist()
