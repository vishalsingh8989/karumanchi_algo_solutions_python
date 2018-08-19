from __future__ import print_function
from tree import Node
from insertNode import insert



def iterativePostorder(root):
    stack = []
    
    while True:
        
        while root is not None:
            if root.right is not None:
                stack.append(root.right)
            stack.append(root)    
            root = root.left
        
        root = stack.pop()
        
        if root.right is not None and stack and stack[-1] == root.right:
            stack.pop()
            stack.append(root)
            root = root.right
        else:
            print(root.data ,  end = " , ")
            root = None
        
        if not stack:
            break
        
         
    

if __name__ == "__main__":
    nums = [3,2,4,5,10,12,7,8,5,1,9,6]
    root = None
    for i in xrange(len(nums)):
        root = insert(root, nums[i])
    
    
    root.prettyPrint()
    
    iterativePostorder(root)
   