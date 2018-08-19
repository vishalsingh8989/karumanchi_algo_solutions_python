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
        
        
    
    
    def find_parent(self, parent, x):
        if parent[x] == -1:
            return x
        return self.find_parent(parent, parent[x])
    
    def union(self, parent, x, y):
        
        x_set = self.find_parent(parent, x)
        y_set = self.find_parent(parent, y)
        parent[x_set] = y_set
    
    def isCyclic(self):
        
        parent = [-1]*self.V
        
        
        for u in self.graph:
            for v in self.graph[u]:
                x = self.find_parent(parent, v)
                y = self.find_parent(parent, u)
                if x != y:
                    self.union(parent, v, u)
                else:
                    print(parent)
                    return True
        print(parent)       
        return False
    
    
    def dfsUtil(self, visited, u):
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
        
    
    

    
if __name__ == "__main__":
    g = Graph(8)
    g.addEdge(0, 1)
    g.addEdge(1, 7)
    g.addEdge(1, 2)
    g.addEdge(2, 3)
    g.addEdge(2, 5)
    g.addEdge(5, 6)
    g.addEdge(3, 4)
    
    
    print(g.isCyclic())
    print(g.dfs())
        
        
        
        