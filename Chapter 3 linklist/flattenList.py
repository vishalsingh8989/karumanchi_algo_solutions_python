from __future__ import print_function
from linklist import printlist


    
def printlist(head):
    print("\nLink list :" ,end = " : ")
    while head is not None:
        print(head.data, end = " -> ")
        head = head.down
        
class Node:
    def __init__(self, data, right, down):
        self.data = data
        self.right = right
        self.down = down


def merge(node_a, node_b):
    if node_a is None:
        return node_b
    if node_b is None:
        return node_a
    
    if node_a.data <= node_b.data:
        head = node_a
        head.down = merge(node_a.down, node_b)
        return head
    else:
        head = node_b
        head.down = merge(node_a, node_b.down)
        return  head

def flatten(head):
    
    if head is None or head.right is None:
        return head
    
    head.right = flatten(head.right)
    
    head = merge(head, head.right)

    return head

if __name__ == "__main__":
    headone = Node(45, None, None)
    headone = Node(40, None, headone)
    headone = Node(35, None, headone)
    headone = Node(28, None, headone)
    
    headtwo = Node(50, None, None)
    headtwo = Node(22, None, headtwo)
    headtwo = Node(19, headone, headtwo)
    
    headthree = Node(20, None, None)
    headthree = Node(10, headtwo, headthree)
    
    headfour = Node(30, None, None)
    headfour = Node(8, None, headfour)
    headfour = Node(7, None, headfour)
    head = Node(5, headthree, headfour)
    
    head = flatten(head)
    printlist(head)
    
    

    
    
    
     