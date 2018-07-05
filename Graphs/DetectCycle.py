"""
"""
from collections import defaultdict


class Graph:
    
    
    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list)
    
    def addEdge(self, u, v):
        self.graph[u].append(v)
        #self.graph[v].append(u)
        
        
    
    def find(self, parent, x):
        if parent[x] == -1:
            return x
        return self.find(parent, parent[x])
        
    
    def union(self, parent, x, y):
        x_set = self.find(parent, x)
        y_set = self.find(parent, y)
        parent[x_set] = y_set
        
     
    def dfsUtil(self, visited, u ):
        
        if visited[u] is True:
            return True
        else:
            visited[u] = True
            
            for v in self.graph[u]:
                if self.dfsUtil(visited, v):
                    return True
            
            visited[u] = False
            
            return False
    
    def dfs(self):
        
        
        visited = [False]*self.V
        
        
        return self.dfsUtil(visited, 0)   

    
    
    def isCyclic(self):
        """https://www.geeksforgeeks.org/union-find/
        """
        parent = [-1]*self.V
        
        for u in xrange(self.V):
            for v in self.graph[u]:
                x = self.find(parent, v)
                y = self.find(parent, u)
                if x!= y:
                    self.union(parent, x, y)
                else:
                    return True
        
        return False
    
if __name__ == "__main__":
    g = Graph(5)
    g.addEdge(0, 1)
    g.addEdge(0, 2)
    g.addEdge(1, 2)
    #g.addEdge(1, 2)
    #g.addEdge(2, 0)
    #g.addEdge(2, 3)
    #g.addEdge(3, 3)
    
    
    print(g.isCyclic())
    print(g.dfs())
        
        
        
        