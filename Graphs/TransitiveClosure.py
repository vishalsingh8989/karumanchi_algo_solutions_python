#!/usr/bin/python
# -*- coding:utf-8 _*_
"""
Given a directed graph, find out if a vertex v is reachable from another 
vertex u for all vertex pairs (u, v) in the given graph. Here reachable 
mean that there is a path from vertex u to v. The reach-ability matrix is 
called transitive closure of a graph.
"""

from collections import defaultdict

class Graph:
    
    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list)
        self.tc = [[0]*self.V for _ in range(self.V)]
    
    def addEdge(self, u, v):
        self.graph[u].append(v)
    
    
    def printMatrix(self):
        for row in self.tc:
            print row
        
    def DFSUtil(self, u , v):
        self.tc[u][v] = 1
        for i in self.graph[v]:
            if self.tc[u][i] == 0:
                self.DFSUtil(u, i)
                
                
    def transitiveClosure(self):
        
        for i in range(self.V):
            self.DFSUtil(i, i)
        
        
        self.printMatrix()
        
if __name__ == "__main__":
    # Create a graph given in the above diagram
    g = Graph(4)
    g.addEdge(0, 1)
    g.addEdge(0, 2)
    g.addEdge(1, 2)
    g.addEdge(2, 0)
    g.addEdge(2, 3)
    g.addEdge(3, 3)
     
    print "Transitive closure matrix is"
    g.transitiveClosure()        
        