from tree import Node
from insertNode import insert, stringToTreeNode

class LNode(Node):
    def __init__(self, vc):
        Node.__init(self, 1)
        self.vc = -1
        

def cover(root):
    
    if root is None:
        return 0
    if root.left is None and root.right is None:
        return 0
    if hasattr(root, "vc"):
        return root.vc
    
    size_excl = 1 + cover(root.left) + cover(root.right)
    
    
    size_incl = 0
    if root.left:
        size_incl += 1 + cover(root.left.left) + cover(root.left.right)
    
    if root.right:
        size_incl += 1 +  cover(root.right.left) + cover(root.right.right)
    
    
    setattr(root, "vc", min(size_excl, size_incl))
#     root.vc = min(size_excl, size_incl)
    
    return root.vc
     
        
        


if __name__ == "__main__":
    nums = [1,2,3,4,5,6,7,8, 9, None, None, 11, None, 12,None,None,None, 13,14,15,16]
    root = stringToTreeNode(nums)
    
    root.prettyPrint()
    print(cover(root))
    