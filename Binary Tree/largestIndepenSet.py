"""
https://www.geeksforgeeks.org/largest-independent-set-problem-dp-26/
"""
from __future__ import print_function
from tree import Node
from insertNode import insert, stringToTreeNode

class LNode(Node):
    def __init__(self, liss, data):
        Node.__init__(self, data)
        self.liss = liss


if __name__ == "__main__":
    nums = [10,20,30,40,None,60,100,70,10,12,13,14,15,16]
    
    lnode = LNode(10, 20)
    
    print(lnode.data, lnode.liss, lnode.left, lnode.right)
    
    root = stringToTreeNode(nums)
    #for i in xrange(len(nums)):
    #    root = insert(root, nums[i])
    
   # 
    root.prettyPrint()