#!/usr/bin/python
__author__ = "Vishal Jasrotia. Stony Brook University"
__copyright__ = ""
__license__ = "GPL"
__version__ = "1.0"
__maintainer__ = "Vishal Jasrotia"
__email__ = "jasrotia.vishal@stonybrook.edu"
__status__ = ""
__problem_number__ = "57"

#imports start
import sys, time
#import end

from linklist import *



def printlist(head):
    while head is not None:
        sys.stdout.write("%d -> "%head.getData())
    print("")


def rightShift(ll, k):
    count = 1
    head = ll.getHead() 
    newhead = head
    newlast = None
    while head is not None and count < k:
        head = head.getNext()
        count+=1

    while head.getNext() is not None:
        newlast = newhead
        newhead = newlast.getNext()
        head = head.getNext()
    
    newlast.setNext(None)
    head.setNext(ll._head)
    ll._head = newhead

    
if __name__ == "__main__":


    ll = LinkList()
    for i in range(15):
        ll.insertAtBegin(i)
    ll.printLinklist()
    rightShift(ll, 3)
    ll.printLinklist()
    rightShift(ll, 3)
    ll.printLinklist()



