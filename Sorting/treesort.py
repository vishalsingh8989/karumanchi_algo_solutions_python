
""" Creates BST then inorder traversal
"""

from sorttest import test
import random
import time
from platform import node

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left_child = None
        self.right_child = None


#iterative
def insert(root, val):
    
    if root is None:
        node = TreeNode(val)
        return node
    else:
        temp = root
        while True:
            if val <=  temp.val:
                if temp.left_child is None:
                    node = TreeNode(val)
                    temp.left_child = node
                    break
                else:
                    temp = temp.left_child
            else:
                if temp.right_child is None:
                    node = TreeNode(val)
                    temp.right_child = node
                    break
                else:
                    temp = temp.right_child
        return root


def inorder(root, res):
    if root is not None:
        inorder(root.left_child, res)
        res.append(root.val)
        inorder(root.right_child, res)


#recursive
def putin(root, val):
    if root is None:
        node = TreeNode(val)
        return node
    else:
        if val <=  root.val:
            root.left_child = putin(root.left_child, val)    
        else:
            root.right_child = putin(root.right_child, val)       
        return root
    
if __name__ == "__main__":
    res = []
    start = time.time()
    for _ in xrange(1000):
        size = random.randint(1,1000)
        nums = [random.randint(-10,30) for _ in xrange(size)]
        root = None
        
        for x in nums:
            root = putin(root, x)
            
        sortlist = []
        inorder(root, sortlist)
        res.append(test(sortlist))
    
   
    end = time.time()
    
    print("%s Pass."%(res.count(True)))
    print("%s Fail."%(res.count(False)))
    print("Time :  %s"%(end-start))





