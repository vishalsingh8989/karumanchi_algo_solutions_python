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


def josephCircle(ll, k):
    head = ll.getHead()
    while head is not None:
        count = 0
        while head is not None and count < k:
            head = head.getNext()
        if head.getNext() is not None and head.getNext().getNext() is not None:

            head.setNext(head.getNext().getNext())

        if len(ll) ==1:
            print("last element is %d"%head.getData())
            break
        else:
            head = ll.getHead()
if __name__ == "__main__":
    ll = LinkList()
    for i in range(15):
        ll.insertAtBegin(i)
    ll.printLinklist()
    josephCircle(ll, 3)

