"""
"""

from linklist import SimpleNode as Node
from linklist import printlist as pl

def reverseList(head):
    prev = None
    curr = head
    while curr is not None:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next

    return prev
    

def rearrange(head):
    slowptr = head
    fastptr = head
    prev = None
    while fastptr is not None and fastptr.next is not None:
        prev = slowptr
        slowptr = slowptr.next
        fastptr = fastptr.next.next

    head1 = head
    head2 = slowptr
    prev.next = None
    
    head2 = reverseList(head2)

    pl(head1)
    pl(head2)
    
    head = Node(-1, None)
    
    curr = head
    while head1 is not None or head2 is not None:
        if head1 is not None:
            curr.next = head1
            curr = curr.next
            head1 = head1.next
        
        if head2 is not None:
            curr.next = head2
            curr = curr.next
            head2 = head2.next
            
    return head.next
   
if __name__ == "__main__":
    
    head = None
    for i in xrange(10, 0, -1):
        node = Node(i, head)
        head = node
    head = rearrange(head)
    pl(head)