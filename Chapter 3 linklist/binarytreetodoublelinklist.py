from __future__ import print_function
from nodes import DoubleNode as Node
from nodes import BTNode
from linklist import printlist
from platform import node

def inorder(root):
    if root is not None:
        inorder(root.left)
        print(str(root.data) , end = " -> ")
        inorder(root.right)

def joinlist(left, right):
    
    if left is None:
        return right
    if right is None:
        return left
    
    leftend = left.prev
    rightend = right.prev
    
    leftend.next = right
    right.prev  = leftend
    
    
    rightend.next = left
    
    left.prev = rightend

    return left

def convertToDouble(root):
    if root is not None:
        right = convertToDouble(root.right)
        left = convertToDouble(root.left)
        
        node = Node(root.data, None, None)
        node.next = node.prev = node
        
        head = joinlist(left, node)
        head = joinlist(head, right)
        
        return head
        

            
if __name__ == "__main__":
    tnodel = BTNode(25, None, None)
    tnoder = BTNode(30, None, None)
    
    tnodel = BTNode(12, tnodel, tnoder)
    tnodel1 = BTNode(36, None, None)
    tnoder1 = BTNode(5, None, None)
    tnoder1 = BTNode(15,tnodel1, tnoder1)
    
    root = BTNode(10,tnodel,tnoder1 )
    inorder(root)
    head = convertToDouble(root)
    
    printlist(head)

    
    
    
    

