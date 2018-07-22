from linklist import DoubleNode as Node, printlist
from random import randint
from mergesortdoublelinklist import mergesort
from platform import node

def reverse(head):
    curr = head
    prev = None
    while curr is not None:
        next = curr.next
        curr.next = prev
        curr.prev = next
        prev = curr
        curr = next
    return prev

def merge(node_a, node_b):
    
    if node_a is  None:
        return node_b
    if node_b is  None:
        return node_a
    
    if node_a.data < node_b.data:
        node = Node(node_a.data, None, None)
        node.next = merge(node_a.next, node_b)
    else:
        node = Node(node_b.data, None, None)
        node.next = merge(node_a, node_b.next)
    
    node.next.prev = node    
    node.prev = None
    return node

def sort(head):
    
    first_half = head
    while first_half.next is not None:
        if first_half.data > first_half.next.data:
            break
        first_half = first_half.next
    
    second_half = first_half.next
    
    first_half.next = None
    second_half.prev = None
    
    first_half = head
    
    printlist(first_half)
    printlist(second_half)
        
    second_half  = reverse(second_half)
    printlist(second_half)
    
    return merge(first_half, second_half)
    

if  __name__ == "__main__":
    prev = None
    head = None
    
    nums = [1,3,5,7,8,9,10,9,8,6,4,2,1,0]
    for i in xrange(len(nums)):
        head = Node(nums[i], prev, head)
        if prev is not None:
            prev.prev = head
        prev = head
    
    head.prev = None
    
    printlist(head)
    
    head = sort(head)
    printlist(head)