
from datastructs import TreeNode, stringToTreeNode
from random import randint

def preorderRec(root, res):
    if root is not None:
        res.append(root.data)
        preorderRec(root.left, res)
        preorderRec(root.right, res)


def preorderItr(root):
    
    if root is None:
        return []
    
    res = []
    stack = []
    stack.append(root)
    
    while stack:
        node = stack.pop()
        
        res.append(node.data)
        
        if node.right is not None:
            stack.append(node.right)
        
        if node.left is not None:
            stack.append(node.left)
        
    return res

if __name__ == "__main__":
    
    res = []
    for i in xrange(1000):
        size = randint(5,100)
        input = [randint(1,100) for i in xrange(size)]
        root = stringToTreeNode(input)
        
        orderRec = []
        preorderRec(root, orderRec)
        
        orderItr = preorderItr(root)
        res.append(orderRec == orderItr)
    
    
    print("%s Pass."%(res.count(True)))
    print("%s Fail."%(res.count(False)))
        

