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
from linklist import *
#import end

def reverselist(head):
    if head is None:
        return None
    elif head.getNext() is None:
        return head
    else:
        rest = reverselist(head.getNext())
        head.getNext().setNext(head)
        head.setNext(None)
        return rest


if __name__ == "__main__":
    ll = LinkList()
    ll.insertAtBegin(60)
    ll.insertAtBegin(50)
    ll.insertAtBegin(40)
    ll.insertAtBegin(30)
    ll.insertAtBegin(20)
    ll.insertAtBegin(10)
    ll.insertAtBegin(0)
    ll.insertAtBegin(-10)
    ll.insertAtBegin(-20)
    ll.insertAtBegin(-30)
    ll.printLinklist()
    newhead = reverselist(ll.getHead())
    print("Reverse link list recursively.")
    while newhead is not None:
        sys.stdout.write("%d"%newhead.getData())
        newhead = newhead.getNext()
        if newhead is not None:
            sys.stdout.write(" -> ")

    print("")
    print(len(ll))
