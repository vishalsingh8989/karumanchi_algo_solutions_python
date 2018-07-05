from __future__ import print_function
from collections import  defaultdict

class Graph:
    
    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list)
        self.inDegree = [0]*self.V
    
    def addEdge(self, u, v):
        self.graph[u].append(v)
        self.inDegree[v] += 1
    
    
    
    
    def topologicalSort(self):
        """
        """
        
        
        queue = []
        for i in xrange(self.V):
            if self.inDegree[i] == 0:
                queue.append(i)
            
        while queue:
            
            u = queue.pop(0)
            print(str(u) + "--> ", end = " ")
            for v in self.graph[u]:
                self.inDegree[v] -=1
                if self.inDegree[v] == 0:
                    queue.append(v)
            
                 
            self.V -= 1
        
        
        if self.V != 0:
            print("Cycle exists  graph")
        

if __name__ == "__main__":
    g = Graph(5)
    
    g.addEdge(0, 1)
    g.addEdge(1, 2)
    g.addEdge(2, 3)
    g.addEdge(3, 4)
    g.addEdge(4, 0)
    g.topologicalSort()
    
    
        
    g= Graph(6)
    g.addEdge(5, 2)
    g.addEdge(5, 0)
    g.addEdge(4, 0)
    g.addEdge(4, 1)
    g.addEdge(2, 3)
    g.addEdge(3, 1)
    
    g.topologicalSort() 
        
            
        
        