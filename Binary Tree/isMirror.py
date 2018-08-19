"""
is Mirror on shape or foldable
"""

from insertNode import insert

def isMirror(node_a, node_b):
    if node_a is None and node_b is None:
        return True
    elif node_a is None or node_b is None:
        return False
    else:
        return isMirror(node_a.left, node_b.right) and isMirror(node_a.right, node_b.left)


if __name__ == "__main__":
    root = None
    for i in xrange(7):
        root = insert(root, i)
    
    
    root.prettyPrint()
    
    print(isMirror(root, root))