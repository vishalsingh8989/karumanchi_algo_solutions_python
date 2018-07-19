from __future__ import print_function
from linklist import SimpleNode as Node
from linklist import printlist
from time import sleep
from random import randint


""" insert node in sorted circular link list
"""

def insert(head, data):
    if head is None:
        head = Node(data, None)
        head.next = head
        return head
    elif data <= head.data:
        curr = head
        while curr.next is not head:
            curr = curr.next
        
        node = Node(data, head)
        curr.next = node
        head = node
        return head
    else:
        curr = head
        while curr.next is not head and data >  curr.next.data:
            curr = curr.next
        
        node = Node(data, curr.next)
        curr.next = node 
        
        return head
        
if __name__ == "__main__":
    head = tail = None
    
    for i in xrange(20):
        head = insert(head, randint(0,100))
    
    printlist(head)
    
    
    