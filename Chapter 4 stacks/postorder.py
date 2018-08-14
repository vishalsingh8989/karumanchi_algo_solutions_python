
from datastructs import TreeNode, stringToTreeNode
from random import randint

def postorderRec(root, res):
    if root:
        postorderRec(root.left, res)
        postorderRec(root.right, res)
        res.append(root.data)
        


def postorderItr(root):
    stack = []
    res = []
    while True:
        while root:
            if root.right is not None:
                stack.append(root.right)
            stack.append(root)
            root = root.left
            
        root = stack.pop()
        
        if root.right is not None and stack and stack[-1]  == root.right:
            stack.pop()
            stack.append(root)
            root = root.right
        else:
            res.append(root.data)
            root = None
        
        if len(stack) == 0 :
            break
    
    return res
            
 
             

if __name__ == "__main__":
    
    
    res = []
    for i in xrange(1000):
        size = randint(5,100)
        input = [randint(1,100) for i in xrange(size)]
        root = stringToTreeNode(input)
    #root.prettyPrint()
        
        orderItr = postorderItr(root)
        orderRec = []
        postorderRec(root, orderRec)
        res.append(orderItr == orderRec)
        
    print("%s Pass."%(res.count(True)))
    print("%s Fail."%(res.count(False)))
        