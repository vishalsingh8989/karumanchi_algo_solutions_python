#!/usr/bin/python
__author__ = "Vishal Jasrotia. Stony Brook University"
__copyright__ = ""
__license__ = "GPL"
__version__ = "1.0"
__maintainer__ = "Vishal Jasrotia"
__email__ = "jasrotia.vishal@stonybrook.edu"
__status__ = ""
  
from collections import defaultdict
  

class Graph:
    
    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list)
    
    
    def addEdge(self, u,v):
        self.graph[u].append(v)
    
    
    def union(self, parent, x, y):
        x_set = self.find(parent, x)
        y_set = self.find(parent, y)
        parent[x_set] = y_set
        
    
    def find(self, parent, x):
        if parent[x] == -1:
            return x
        return self.find(parent, parent[x])

    
    def isCyclic(self):
        
        parent = [-1]*self.V
        
        for i in self.graph:
            for j in self.graph[i]:
                x = self.find(parent, i)
                y = self.find(parent, j)
                if x == y:
                    return True
                self.union(parent, x, y)
                
                
    
 
# Create a graph given in the above diagram

if __name__ == "__main__": 
    g = Graph(6)
    g.addEdge(0, 1)
    g.addEdge(0, 2)
    g.addEdge(1, 3)
    g.addEdge(1, 5)
    g.addEdge(3, 4)
    g.addEdge(3, 1)
    if g.isCyclic():
        print "Graph contains cycle"
    else :
        print "Graph does not contain cycle "
  