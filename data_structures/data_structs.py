class Queue:
    
    def __init__(self):
        self.q = []
        
    def push(self, val):
        self.q.append(val)
    
    def pop(self):
        return self.q.pop(0)
    
    
    def isempty(self):
        return len(self.q) == 0
    
    def show(self):
        print(self.q)
    



class Stack:
    def __init__(self):
        self.q = []
        
    def push(self, val):
        self.q.append(val)
    
    def pop(self):
        return self.q.pop()
    
    def isempty(self):
        return len(self.q) == 0
    
    def show(self):
        print(self.q)
    