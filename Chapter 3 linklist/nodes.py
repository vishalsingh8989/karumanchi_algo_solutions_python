
class BTNode:
    def __init__(self, data, left, right):
        self.data = data
        self.left = left
        self.right = right
    
    
class DoubleNode:
    def __init__(self, data, prev, next):
        self.data = data
        self.next = next
        self.prev = prev

    def __repr__(self):
        if self.next is None:
            next =  "next(None)"
        else:
            next = "next(" +str()+ ")"
             
        if self.prev is None:
            prev = "prev(None)"
        else:
            prev = "prev(" +str(self.prev.data)+ ")"
            
        rpr = "[ " + prev + ", " +str(self.data) + ", " + next + " ]" 
        return rpr
     
class SimpleNode:
    def __init__(self, data, next):
        self.data = data
        self.next = next
    
    def __repr__(self):
        if self.next is None:
            rpr = " [ "+str(self.data) + ", next(None) ] "
        else:
            rpr = " [ "+str(self.data) + ", next("+str(self.next.data)+") ] "
        return rpr