"""
https://www.geeksforgeeks.org/linked-list-in-zig-zag-fashion/
"""
from linklist import SimpleNode as Node
from linklist import printlist
import random
import time

def mklist(initializer):
    head = temp = Node(initializer[0], None)
    for i in xrange(1, len(nums)):
        n = Node(initializer[i], None)
        temp.next = n
        temp = temp.next
    return head

def swap(node_a, node_b):
    
    node_a.data, node_b.data = node_b.data,  node_a.data

def zigzagorder(head):
    flag = True
    curr= head
    
    while curr.next is not None:
        if flag and curr.data > curr.next.data:
            swap(curr, curr.next)
        if not flag and curr.data < curr.next.data:
            swap(curr, curr.next)
            
        flag = not flag
        curr = curr.next
    return head
            
            
    

if __name__ == "__main__":
    
    res = []
    start = time.time()
    for _ in xrange(1):
        size = random.randint(10,15)
        nums = [random.randint(0,100) for _ in xrange(size)]
        head = mklist(nums)
        printlist(head)
        head = zigzagorder(head)
        printlist(head)
        