
from collections import defaultdict

class Graph:
    
    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list)
    
    def addEdge(self, u, v):
        self.graph[u].append(v)


    def isOddCycle(self):
        color = [-1]*self.V
        color[0] = 0 
        
        
        queue = []
        queue.append(0)
        
        while queue:
            u = queue.pop(0)
            for v in self.graph[u]:
                if color[v] == -1:
                    color[v] = 1 -  color[u]
                    queue.append(v)
                elif color[v] == color[u]:
                    return True
        
        return False 
                
        
if __name__ == "__main__":
    
    g = Graph(5)
    
    g.addEdge(0, 1)
    g.addEdge(1, 2)
    g.addEdge(2, 3)
    g.addEdge(3, 4)
    g.addEdge(4, 0)
    
    print(g.isOddCycle())
    
    g = Graph(5)
    
    g.addEdge(0, 1)
    g.addEdge(1, 2)
    g.addEdge(2, 3)
    g.addEdge(3, 0)
    g.addEdge(4, 0)
    print(g.isOddCycle())