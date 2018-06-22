#!/usr/bin/python
"""
"""
from __future__ import print_function
from collections import defaultdict



class Graph:
    
    
    def __init__(self):
        """
        """
        
        self.graph = defaultdict(list)
    
    def addEdge(self, u, v):
        """
        """
        self.graph[u].append(v)
    
    
    def BFS(self, src):
        """
        """
        visited = [False]*len(self.graph)
        
        queue = []
        queue.append(src)
        
        while queue:
            u = queue.pop(0)
            visited[u] = True
            print(str(u) + " -> ", end = " " )
            
            for v in self.graph[u]:
                if visited[v] is False:
                    queue.append(v)
                
if __name__ == "__main__":
    g = Graph()
    g.addEdge(0, 1)
    g.addEdge(0, 2)
    g.addEdge(1, 2)
    g.addEdge(2, 0)
    g.addEdge(2, 3)
    g.addEdge(3, 3)
     
    print ("Following is Breadth First Traversal"
                      " (starting from vertex 2)")
    g.BFS(2)
                
                
                
            