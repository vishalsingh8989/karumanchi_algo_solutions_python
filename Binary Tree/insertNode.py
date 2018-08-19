from tree import Node

def insert(root, key):
    if root is None:
        return Node(key)
    else:
        queue = [root]
        while queue:
            size = len(queue)
            
            for i in xrange(size):
                node = queue.pop(0)
                if node.left is not None:
                    queue.append(node.left)
                else:
                    node.left = Node(key)
                    return root
                if node.right is not None:
                    queue.append(node.right)
                else:
                    node.right = Node(key)
                    return root
    
    




if __name__ == "__main__":
    root = None
    for i in xrange(31):
        root = insert(root, i)
    
    root.prettyPrint()
    
    


    