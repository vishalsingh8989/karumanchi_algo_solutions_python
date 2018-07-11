from __future__ import print_function
from linklist import SimpleNode as Node
from linklist import printlist
import random

def getLength(head):
    count = 0
    while head is not None:
        head = head.next
        count +=1
    return count

def merge(node_a, node_b):
    if node_a is None:
        return node_b
    if node_b is None:
        return node_a
    
    if node_a.data >= node_b.data:
        head = node_a
        head.next = merge(node_a.next, node_b)
        return head
    else:
        head = node_b
        head.next = merge(node_a, node_b.next)
        return head
    
def mergesort(head):
    mid = getLength(head)/2
    
    if head.next is None:
        return head
    first_head = head
    while mid - 1 >  0:
         first_head = first_head.next
         mid -=1
        
    second_head = first_head.next
    first_head.next = None
    first_head = head
    
    node_a = mergesort(first_head)
    node_b = mergesort(second_head)
    
    return merge(node_a, node_b)
    


if __name__ == "__main__":
    head = Node(random.randint(1,100), None)
    for i in xrange(1,20):
        node = Node(random.randint(1,100), head)
        head = node
    printlist(head)
    head = mergesort(head)
    printlist(head)