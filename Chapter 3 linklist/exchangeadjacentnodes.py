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

from linklist import *

def exchangeadjacent(ll):
    low = ll.getHead()
    high = low.getNext()
    while low is not None and high is not None:
        lowval = low.getData()
        highval = high.getData()
        low.setData(highval)
        high.setData(lowval)
        low = high.getNext()
        if low is None:
            break
        else:
            high  = low.getNext()


if __name__== "__main__":
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
    ll.printLinklist()
    exchangeadjacent(ll)
    ll.printLinklist()
