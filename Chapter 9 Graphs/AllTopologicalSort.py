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
    
    
    def topologicalSortUtil(self, result, visited):
        
        flag = True
        
        for i in xrange(self.V):
            if visited[i] is False and self.inDegree[i] == 0:
                for v in self.graph[i]:
                    self.inDegree[v] -=1
                
                visited[i] = True
                self.topologicalSortUtil(result + [i], visited)
                visited[i] = False
                
                for v in self.graph[i]:
                    self.inDegree[v] +=1 
                
                flag = False
        
        if flag is True:
            print(result)
    
    def topologocalSort(self):
        visited = [False]*self.V
        result = []
        self.topologicalSortUtil(result, visited)
            
if __name__ == "__main__":
    g =  Graph(6)
    g.addEdge(5, 2)
    g.addEdge(5, 0)
    g.addEdge(4, 0)
    g.addEdge(4, 1)
    g.addEdge(2, 3)
    g.addEdge(3, 1)
 
    print( "All Topological sorts")
 
    g.topologocalSort();
      
        
        
        