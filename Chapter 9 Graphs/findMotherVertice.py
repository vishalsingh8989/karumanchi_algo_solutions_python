#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
https://www.geeksforgeeks.org/find-a-mother-vertex-in-a-graph/
A mother vertex in a graph G = (V,E) is a vertex v such that all other vertices in G can be reached by a path from v.
Algorithm :

Do DFS traversal of the given graph. While doing traversal keep track of last finished vertex ‘v’. This step takes O(V+E) time.
If there exist mother vertex (or vetices), then v must be one (or one of them). Check if v is a mother vertex by doing DFS/BFS from v. This step also takes O(V+E) time.

"""

from collections import defaultdict

class Graph:
    
    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list)
    
    def addEdge(self, u, v):
        self.graph[u].append(v)
    
    
    def DFSUtil(self, v, visited):
        
        visited[v] = True
        
        for i in self.graph[v]:
            if visited[i] is False:
                self.DFSUtil(i, visited)
    
    def findMother(self):
        
        visited = [False]*self.V
        v = 0 
        
        for i in range(self.V):
            if visited[i] is False:
                self.DFSUtil(i, visited)
                v = i  # candidate  who finish last could be mother of all vertices
        
        
        # test candidate
        # Reset all values in visited[] as false and do
        # DFS beginning from v to check if all vertices are
        # reachable from it or not.       
        visited = [False]*self.V
        self.DFSUtil(v, visited)
        if any( i is False for i in visited):
            return -1
        else:
            return v
        
        
if __name__ == "__main__":
    # Create a graph given in the above diagram
    g = Graph(7)
    g.addEdge(0, 1)
    g.addEdge(0, 2)
    g.addEdge(1, 3)
    g.addEdge(4, 1)
    g.addEdge(6, 4)
    g.addEdge(5, 6)
    g.addEdge(5, 2)
    g.addEdge(6, 0)
    print "A mother vertex is " + str(g.findMother())        
        
                
        
            
        
        
        