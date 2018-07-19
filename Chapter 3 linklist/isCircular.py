from __future__ import print_function
from linklist import SimpleNode as Node
from linklist import printlist
from time import sleep

def isCircular(head):
    curr = head
    if head is None:
        return False
    
    while curr.next is not None and curr.next is not head:
        curr = curr.next
    
    if curr.next is head:
        return True
    else:
        return False

if __name__ == "__main__":
    head = tail = Node(10, None)
    for i in xrange(10):
        head = Node(i, head)
    
    printlist(head)
    print("iscircular , " , isCircular(head))
    tail.next = head
    
    printlist(head)
    print("iscircular , " , isCircular(head))
    