#!/usr/bin/python
# -*- coding : utf-8 -*-
"""
"""
from __future__ import print_function
from collections import defaultdict

class Graph:
    
    
    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list)
    
    
    def addEdge(self, u, v):
        self.graph[u].append(v)
    
    def DFSIterative(self, src):
        
        
        visited = [False]*self.V
        stack = []
        
        stack.append(src)
        visited[src] = True
        
        
        while stack:
            
            u = stack.pop()
            visited[u] = True
            print(str(u) + " -- > " ,end = " ")
            
            for v in self.graph[u]:
                if visited[v] is False:
                    stack.append(v)
                    
                    
                    
if __name__ == "__main__":
    g = Graph(5)
    g.addEdge(1, 0)
    g.addEdge(0, 2)
    g.addEdge(2, 1)
    g.addEdge(0, 3)
    g.addEdge(1, 4)
 
    print( "Following is Depth First Traversal")
    g.DFSIterative(0)