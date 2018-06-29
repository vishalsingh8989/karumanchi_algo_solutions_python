#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
https://www.geeksforgeeks.org/check-if-two-nodes-are-on-same-path-in-a-tree/
"""


from collections import defaultdict


class Graph:
    
    def __init__(self, vertices):
        self.V =  vertices
        self.graph = defaultdict(list)
        self.inTime = {}
        self.outTime = {}
        self.t = 0
    def addEdge(self, u, v):
        self.graph[u].append(v)
    
    
    def dfs(self, u):
        
        visited = [False]*self.V
        self.dfsUtil(u, visited)
        
        print(self.inTime)
        print(self.outTime)
        
    
    def dfsUtil(self, u, visited):
        visited[u] = True
        self.inTime[u] = self.t
        self.t +=1
        for v in self.graph[u]:
            if visited[v] is False:
                self.dfsUtil(v, visited)
        self.outTime[u] = self.t
        
           
    def query(self, v, u):
        if (self.inTime[u] < self.inTime[v] and self.outTime[u] >  self.outTime[v]) or (self.inTime[v] < self.inTime[u] and self.outTime[v] >  self.outTime[u]):
            return True
        return False
    
if __name__ == "__main__":
    n = 7
    g = Graph(n)
    g.addEdge(0, 1)
    g.addEdge(0, 2)
    g.addEdge(0, 3)
    g.addEdge(1, 4)
    g.addEdge(2, 5)
    g.addEdge(3, 6)
    
    
   
    g.dfs(0)
    
    print(g.query(0, 4)) 
    print(g.query(0, 2))
    print(g.query(4, 5))

    
    
    
    