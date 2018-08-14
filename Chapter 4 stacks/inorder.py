
from datastructs import TreeNode, stringToTreeNode
from random import randint

def inorderRec(root, res):
    if root:
        inorderRec(root.left, res)
        res.append(root.data)
        inorderRec(root.right, res)



def inorderItr(root):
    
   
    res = []
    stack = []
   
    while True:
        if root is not None:
            stack.append(root)
            root = root.left
        else:
            if stack:
                root = stack.pop()
                res.append(root.data)
                root = root.right
            else:
                break
    
    return res
                

if __name__ == "__main__":
    
    
    res = []
    for i in xrange(100):
        size = randint(5,100)
        input = [randint(1,100) for i in xrange(size)]
        root = stringToTreeNode(input)
        orderItr = inorderItr(root)
        orderRec = []
        inorderRec(root, orderRec)
        res.append(orderRec == orderItr)
        
    print("%s Pass."%(res.count(True)))
    print("%s Fail."%(res.count(False)))
        
    
    