from __future__ import print_function
from tree import Node
from insertNode import insert

def iterativePreorder(root):
    
    stack = [root]
    
    
    while stack:
        node = stack.pop()
        
        print(node.data , end = ", ")
        
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
        


if __name__ == "__main__":
    nums = [3,2,4,5,10,12,7,8,5,1,9,6, 11,13,14]
    
    root = None
    for i in xrange(len(nums)):
        root = insert(root, nums[i])
    
    
    root.prettyPrint()
    iterativePreorder(root)
        
        
        
        