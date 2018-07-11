"""
https://www.geeksforgeeks.org/delete-nodes-which-have-a-greater-value-on-right-side/
"""
from __future__ import print_function
from linklist import SimpleNode as Node
from linklist import printlist
from random import randint
from sys import maxint

def deleteMax(head):
    head = reverse(head)
    printlist(head)
    maxval = -1*maxint
    curr = head
    prev = None
    while curr is not None and curr.next is not None:
        if curr.next.data <  maxval:
            temp = curr.next
            curr.next = temp.next
            del temp
        else:
            curr = curr.next
            maxval = max(maxval, curr.data)
    
    head = reverse(head)
    return head

def reverse(head):
    curr = head
    prev = None
    while curr is not None:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next
    
    return prev


if __name__ == "__main__":
    head = None
    for i  in xrange(0, 21):
        node = Node(randint(1,100), head)
        head = node
    printlist(head)
    head = deleteMax(head)
    printlist(head)
        
    