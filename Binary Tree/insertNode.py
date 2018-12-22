from tree import Node 

def stringToTreeNode(input):
    #input = input.strip()
    #input = input[1:-1]
    if not input:
        return None

    inputValues = input #[s.strip() for s in input.split(',')]
    root = TreeNode(int(inputValues[0]))
    nodeQueue = [root]
    front = 0
    index = 1
    while index < len(inputValues):
        node = nodeQueue[front]
        front = front + 1

        item = inputValues[index]
        index = index + 1
        if item != "null"  and item is not None:
            leftNumber = int(item)
            node.left = TreeNode(leftNumber)
            nodeQueue.append(node.left)

        if index >= len(inputValues):
            break

        item = inputValues[index]
        index = index + 1
        if item != "null"  and item is not None:
            rightNumber = int(item)
            node.right = TreeNode(rightNumber)
            nodeQueue.append(node.right)
    return root


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
    
    


    