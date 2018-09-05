"""
Construct Tree from given Inorder and Preorder traversals
Let us consider the below traversals:

Inorder sequence: D B E A F C
Preorder sequence: A B D E C F
"""

from __future__ import print_function
from tree import Node
from insertNode import insert


def search(inorder, val, low, high):
    for i in xrange(low, high+1):
        if inorder[i] == val:
            return i 
    
def buildTree(inorder, preorder, low, high):
    
    if low >  high:
        return None
    
    node = Node(preorder[buildTree.preorderIndex])
    
    index = search(inorder, preorder[buildTree.preorderIndex], low, high)
    buildTree.preorderIndex +=1
    
    node.left = buildTree(inorder, preorder, low, index - 1)
    node.right = buildTree(inorder, preorder, index + 1, high)
    
    return node


if __name__ == "__main__":
#     nums = [3,2,4,5,10,12,7,8,5,1,9,6, 11,13,14]
#     root = None
#     for i in xrange(len(nums)):
#         root = insert(root, nums[i])
#     
#     
#     root.prettyPrint()
    
    buildTree.preorderIndex = 0
    preorder = [3, 2, 5, 8, 5, 10, 1, 9, 4, 12, 6, 11, 7, 13, 14,]
    inorder = [8 , 5 , 5 , 2 , 1 , 10 , 9 , 3 , 6 , 12 , 11 , 4 , 13 , 7 , 14]
    
    root = buildTree(inorder, preorder, 0, len(inorder)-1)
    root.prettyPrint()

