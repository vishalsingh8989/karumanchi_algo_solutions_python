#!/usr/bin/python
from __future__ import print_function
__author__ = "Vishal Jasrotia. Stony Brook University"
__copyright__ = ""
__license__ = "GPL"
__version__ = "1.0"
__maintainer__ = "Vishal Jasrotia"
__email__ = "jasrotia.vishal@stonybrook.edu"
__status__ = ""

from linklist import Node
import sys
import random



def getLength(root):
    count = 0
    while root is not None:
        count +=1
        root = root.getNext()
    return count


def merge(node_a, node_b):
    head = None
    if node_a is None:
        return node_b
    if node_b is None:
        return node_a
    if node_a.getData() >= node_b.getData():
        head = node_b
        next_node = merge(node_a, node_b.getNext())
        node_b.setNext(next_node)
    else:
        head = node_a
        next_node = merge(node_a.getNext(), node_b)
        node_a.setNext(next_node)
    return head
        
def mergesort(node):
    mid = getLength(node)/2
    
    first_head = node
    if node.getNext() is None:
        return node
    
    while mid - 1 > 0:
        first_head = first_head.getNext()
        mid -= 1
    
    second_head = first_head.getNext()
    
    first_head.setNext(None)
    first_head = node
    
    node_a = mergesort(first_head)
    node_b = mergesort(second_head)
    
    return merge(node_a, node_b)
    

        
def mklist(initializer):
    head = temp = Node(initializer[0], None)
    for i in xrange(1, len(nums)):
        n = Node(initializer[i], None)
        temp.setNext(n)
        temp = temp.getNext()
    return head

def walk(head):
    while head is not None:
        yield head.getData()
        head = head.getNext()

if __name__ == "__main__":
    nums = [20, 1, 9, 15, 12, 3, 2, 11, 2, 8, 12, 13, 7, 3, 3, 5, 11, 4, 9, 2]
    
    root = mklist(nums)
    for x in walk(root):
        print(str(x) + " -> ", end='')
    print(len(nums), getLength(root))
    
    root = mergesort(root)
    for x in walk(root):
        print(str(x) + " -> ", end='')
    print(len(nums), getLength(root))
     
    
        