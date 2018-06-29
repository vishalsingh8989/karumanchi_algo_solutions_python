"""
https://www.geeksforgeeks.org/minimum-number-of-edges-between-two-vertices-of-a-graph/
"""
from __future__ import print_function
from _collections import defaultdict
from sys import maxint

class Graph:
    
    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list)
    
    def addEdge(self, u, v):
        self.graph[u].append(v)
    
    def minDist(self, dist, sptSet):
        min = maxint
        for i in xrange(len(dist)):
            if sptSet[i] is False and min >= dist[i]:
                min_index = i
                min = dist[i]
        #print("min : " ,  min_index)
        return min_index
        
    
    def minPath(self, src, dst):
        #print(self.graph)
        
        dist = [maxint]*self.V
        sptSet = [False]*self.V
        dist[src] = 0
        parent = [-1]*self.V
        
        
        for count in xrange(self.V):
             u = self.minDist(dist, sptSet)
             sptSet[u] = True
             for v in self.graph[u]:
                 if sptSet[v] is False and dist[u] + 1 <  dist[v]:
                     dist[v] = dist[u] + 1
                     parent[v] = u 
        
        
        
        curr = 5
        while curr != -1:
            print(str(curr) + " <--- " , end = '')
            curr = parent[curr]
        print()
        return dist[dst]


if __name__ == "__main__":
    g = Graph(9)
    g.addEdge( 0, 1)
    g.addEdge( 0, 7)
    g.addEdge( 1, 7)
    g.addEdge( 1, 2)
    g.addEdge( 2, 3)
    g.addEdge( 2, 5)
    g.addEdge( 2, 8)
    g.addEdge( 3, 4)
    g.addEdge( 3, 5)
    g.addEdge( 4, 5)
    g.addEdge( 5, 6)
    g.addEdge( 6, 7)
    g.addEdge( 7, 8)
    u = 0
    v = 5
    hops = g.minPath(u, v)
    print("number of hops: ", hops)
    
                 
                 
                 
        
        
        