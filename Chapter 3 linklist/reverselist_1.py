from __future__ import print_function
from linklist import SimpleNode as Node

from linklist import printlist
def reverselistRec(curr, prev):
    
    if curr is None:
        return prev

    next = curr.next
    curr.next = prev 
    return reverselistRec(next, curr)


def reverselist(head):
    curr = head
    prev = None
    while curr is not None:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next
    return prev    
    
    
if __name__ == "__main__":
    
    head = Node(0, None)
    for i in xrange(1,10):
        node = Node(i, head)
        head = node
    
    printlist(head)
    head = reverselist(head)
    printlist(head)
    head = reverselistRec(head, None)
    printlist(head)