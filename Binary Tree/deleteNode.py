from insertNode import insert

def deleteLast(root, last_val):
    
    queue = [root]
    
    while queue:
        size = len(queue)
        for i in xrange(size):
            node = queue.pop(0)
            if node.left:
                if node.left.data == last_val:
                    del node.left
                    node.left = None
                    return 
                else:
                    queue.append(node.left)
            
            if node.right:
                if node.right.data == last_val:
                    del node.right
                    node.right = None
                    return 
                else:
                    queue.append(node.right)
            
                
                    
    
def deleteNode(root, val):
    
    queue = [root]
    
    while queue:
        size = len(queue)
        for i in xrange(size):
            node = queue.pop(0)
            if node.data == val:
                key_node = node
            
            if node.left:
                queue.append(node.left)
            
            if node.right:
                queue.append(node.right)
    
    last_val = node.data
    
    deleteLast(root, last_val)
    key_node.data = last_val
    return root
    
    
    
if __name__ == "__main__":
    root = None
    for i in xrange(31):
        root = insert(root, i)
    
    root.prettyPrint()
    
    root = deleteNode(root, 5)
    root.prettyPrint()
    
    
