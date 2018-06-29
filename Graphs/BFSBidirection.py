#!/usr/bin/python
# -*- coding :utf-8 -*-
"""
https://www.geeksforgeeks.org/bidirectional-search/
"""
from __future__ import print_function
from collections import defaultdict

class Graph:
    
    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list)
    
    def addEdge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)
    
    def printParent(self, s, d, i, s_parent, d_parent):
        u = i
        path = []
        while u != -1:
            path.insert(0, u)
            u = s_parent[u]
        
        while len(path) != 1:
            u = path.pop(0)
            print(str(u) + " -- > " , end = " ")
        u = i
        while u != -1:
            print(str(u) + " -- > " , end = " ")
            u = d_parent[u]
        
    def isIntersecting(self, s_visited, d_visited ):
        for i  in xrange(len(s_visited)):
            if s_visited[i] is True and d_visited[i] is True:
                return i
        return -1
    
    def BFSUtil(self, queue, visited, parent):    
        
        u = queue.pop(0)
        for v in self.graph[u]:
            
            if visited[v] is False:
                queue.append(v)
                parent[v] = u 
                visited[v] = True       
    
    
    def BiSearch(self, s, d):
        s_queue = []
        s_visited = [False]*self.V
        s_parent = [None]*self.V
        
        
        d_queue = []
        d_visited = [False]*self.V
        d_parent = [None]*self.V
        
        
        #init
        s_queue.append(s)
        s_parent[s] = -1
        s_visited[s] = True
        
        d_queue.append(d)
        d_parent[d] = -1
        d_visited[d] = True
        
        
        while  s_queue and d_queue:
            self.BFSUtil(s_queue, s_visited, s_parent)
            self.BFSUtil(d_queue, d_visited, d_parent)
            i = self.isIntersecting(s_visited, d_visited)
            if i != -1:
                print("Path between {0} and {1} intersect at {2}".format(s, d, i))
                self.printParent(s,d,i, s_parent, d_parent)
                break
                
        print("Done")   
        
        

if __name__ == "__main__":
    
    
    n=15
    s=0
    d=14
    g = Graph(n)

    g.addEdge(0, 4)
    g.addEdge(1, 4)
    g.addEdge(2, 5)
    g.addEdge(3, 5)
    g.addEdge(4, 6)
    g.addEdge(5, 6)
    g.addEdge(6, 7)
    g.addEdge(7, 8)
    g.addEdge(8, 9)
    g.addEdge(8, 10)
    g.addEdge(9, 11)
    g.addEdge(9, 12)
    g.addEdge(10, 13)
    g.addEdge(10, 14)
    
    g.BiSearch(s, d)
        
        
