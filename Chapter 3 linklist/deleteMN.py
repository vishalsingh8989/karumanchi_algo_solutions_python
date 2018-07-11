"""
https://www.geeksforgeeks.org/delete-n-nodes-after-m-nodes-of-a-linked-list/
"""
from __future__ import print_function
from linklist import SimpleNode as Node
from linklist import printlist


def deleteMN(head, m , n):
    
    curr = head 
    
    while curr is not None:
        
        for i in xrange(m-1):
            curr = curr.next
            if curr is None:
                break
        
        if curr is None:
            return
        
        curr_next = curr.next
        
        for i in xrange(n):
            curr_next = curr_next.next
            if curr_next is None:
                break
        if curr_next is None:
            break
        
        curr.next  = curr_next
        curr = curr_next
        
        
    
    
if __name__ == "__main__":
    head = None
    for i in xrange(20, -1, -1 ):
        node = Node(i, head)
        head = node
    printlist(head)
    
    deleteMN(head, 3, 2)
    printlist(head)