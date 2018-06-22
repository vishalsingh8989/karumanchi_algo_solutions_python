#!/usr/bin/python
# -*- coding:utf-8 -*-
"""
Count the total number of ways or paths that exist between two vertices in a directed graph. 
These paths doesn’t contain a cycle, the simple enough reason is that a cylce contain infinite 
number of paths and hence they create problem.
https://www.geeksforgeeks.org/count-possible-paths-two-vertices/
"""

from collections import defaultdict


class Graph:
    
    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list)
    
    def addEdge(self, u,v):
        self.graph[u].append(v)
    
    
    def count(self, src, dst):
        visited = [False]*self.V
        self.PathCount(src, dst, visited, [])
        
    def PathCount(self, src, dst, visited, path):
        visited[src] = True
        if src == dst:
            print(path)
        else:
            for v in self.graph[src]:
                if visited[v] is False:
                    self.PathCount(v, dst, visited, path + [src])
        visited[src] = False
    
if __name__ == "__main__":
    g =  Graph(4);
    g.addEdge(0, 1)
    g.addEdge(0, 2)
    g.addEdge(0, 3)
    g.addEdge(2, 0)
    g.addEdge(2, 1)
    g.addEdge(1, 3)
    
    s = 2
    d = 3
    
    g.count(s, d)
 
            
        