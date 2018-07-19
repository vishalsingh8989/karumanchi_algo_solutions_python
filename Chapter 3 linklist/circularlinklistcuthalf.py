from __future__ import print_function
from linklist import SimpleNode as Node
from linklist import printlist
from time import sleep


def cutHalf(head):
    slowptr = head
    fastptr = head
    
    while fastptr.next != head and fastptr.next.next != head:
        slowptr = slowptr.next
        fastptr = fastptr.next.next
    
    if fastptr.next.next == head:
        fastptr = fastptr.next
    
    firsthead = slowptr.next
    slowptr.next = None
    
    fastptr.next = None
    
    return head, firsthead
    
if __name__ == "__main__":
    head = tail = Node(10, None)
    for i in xrange(9, -1, -1):
        head = Node(i, head)
    
    tail.next = head
    printlist(head)
    head1, head2 = cutHalf(head)
    printlist(head1)
    printlist(head2)
    