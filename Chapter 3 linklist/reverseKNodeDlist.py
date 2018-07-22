from linklist import DoubleNode as Node, printlist
from random import randint
from linklist import isLinkListSorted


def reverseKNode(head, k):
    
    if head is not None:
        prev = None
        curr = head
        c = 0
        while curr is not None and c < k:
            next = curr.next
            curr.next = prev
            curr.prev = next
            prev = curr
            curr = next
            c +=1
        
        if next is not None:
            head.next = reverseKNode(next, k)
            head.next.prev = head
        else:
            head.next = None
        
        return prev
        
if __name__ == "__main__":
    prev = None
    head = None             
    for i in xrange(10):
        head = Node(randint(2,10), prev, head)
        if prev is not None:
            prev.prev = head
        prev = head
    
    head.prev = None
    printlist(head)
    head = reverseKNode(head, 4)
    printlist(head)
             