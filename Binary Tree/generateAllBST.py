"""

Find all possible binary trees with given Inorder Traversal
"""


from tree import Node

def getTree(inorder, start, end):
    
    trees = []
    if start >  end:
        trees.append(None)
        return trees
    
    for i in xrange(start, end+1):
        lftree = getTree(inorder, start, i-1)
        rttree = getTree(inorder, i+1, end)
        
        
        for lt  in lftree:
            for rt in rttree:
                
                node = Node(inorder[i])
                node.left = lt
                node.right = rt
                
                
                trees.append(node)
    
    return trees
         


if __name__ == "__main__":
    inorder = [4,5,6,7,8]
    
    trees = getTree(inorder, 0, len(inorder)-1)
    print(len(trees))
    for root in trees:
        root.prettyPrint()
    