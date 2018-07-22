"""https://www.geeksforgeeks.org/remove-duplicates-sorted-doubly-linked-list/
"""
from linklist import DoubleNode as Node, printlist
from random import randint
from mergesortdoublelinklist import mergesort



def removeDup(head):
    
    new_head = Node(head.data, None, None)
    tail = new_head
    
    head  = head.next
    while head is not None:
        if head.data != tail.data:
            node = Node(head.data, tail, None)
            tail.next = node
            tail = tail.next
        head = head.next
    
    return new_head

if __name__ == "__main__":
    prev = None
    head = None
    
    for i in xrange(12):
        head = Node(randint(1,8), prev, head)
        if prev is not None:
            prev.prev = head
        prev = head
        
    head.prev = None
    printlist(head)
    
    head = mergesort(head)
    printlist(head)
    head = removeDup(head)
    printlist(head)
    