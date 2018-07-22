from linklist import DoubleNode as Node, printlist, printlistrev
from random import randint
from linklist import isLinkListSorted


def reverse(head):
    prev = None
    curr = head
    
    while curr is not None:
        next = curr.next
        curr.next = prev
        curr.prev = next
        prev = curr
        curr = next
    
    return prev


if __name__ == "__main__":
    
    prev = None
    head = None
    for i in xrange(10, 0 ,  -1):
        head = Node(i, prev, head)
        if prev is not None:
            prev.prev = head
        prev = head
        
    head.prev = None
    
    tail = printlist(head)
    head = reverse(head) 
    printlist(head)
        
    
