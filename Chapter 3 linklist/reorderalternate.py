#!/usr/bin/python
__author__ = "Vishal Jasrotia. Stony Brook University"
__copyright__ = ""
__license__ = "GPL"
__version__ = "1.0"
__maintainer__ = "Vishal Jasrotia"
__email__ = "jasrotia.vishal@stonybrook.edu"
__status__ = ""
__problem_number__ = "54"

#imports start
import sys, time
#import end

from linklist import *


def printlist(head):
    while head is not None:
        sys.stdout.write("%d -> "%head.getData())
        head = head.getNext()
    print("")

def splitlist(ll):
    slow = ll.getHead()
    fast = slow.getNext()
    slowprev = None
    count = 0
    while fast is not None:
        if count%2 == 0 :
            slowprev = slow
            slow = slow.getNext()
            fast = fast.getNext()
        else:
            fast = fast.getNext()
        count+=1
    slowprev.setNext(None)
    return ll.getHead(), slow # head of original list and head of middle element

def reorderList(ll):
    head1, head2 = splitlist(ll)

    #printlist(head1)
    #printlist(head2)

    altlist = LinkList()
    count  = 0
    while head1 is not None  and head2 is not None:
        if count%2 == 0 :
            #print("Adding %d ."%head1.getData())
            altlist.insertAtBegin(head1.getData())
            head1 = head1.getNext()
        else:
            #print("Adding %d ."%head2.getData())
            altlist.insertAtBegin(head2.getData())
            head2 = head2.getNext()
        count+=1

    while head1 is not None:
        #print("Adding rem %d."%head1.getData())
        altlist.insertAtBegin(head1.getData())
        head1 = head1.getNext()
    while head2 is not None:
        #print("Adding rem %d."%head2.getData())
        altlist.insertAtBegin(head2.getData())
        head2 = head2.getNext()

    print("New reorderd list is :")
    altlist.printLinklist()



if __name__=="__main__":
    ll = LinkList()
    for i in range(15):
        ll.insertAtBegin(i)
    ll.printLinklist()
    reorderList(ll) 









