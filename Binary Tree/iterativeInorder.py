from __future__ import print_function
from tree import Node
from insertNode import insert


def iterativeInorder(root):
    flag =  True
    
    stack = []
    
    while flag:
        if root is not None:
            stack.append(root)
            root = root.left
        else:
            
            if stack:
                root = stack.pop()
                print(root.data, end = " , ")
                root = root.right
            else:
                flag = False
                

if __name__ == "__main__":
    nums = [3,2,4,5,10,12,7,8,5,1,9,6,None, 11,13,14]
    root = None
    for i in xrange(len(nums)):
        root = insert(root, nums[i])
    
    
    root.prettyPrint()
    iterativeInorder(root)