#!/usr/bin/python
# -*- coding: utf-8 -*-
"""

Algorithm
1) Create a set sptSet (shortest path tree set) that keeps track of vertices included in shortest path tree, i.e., whose minimum distance from source is calculated and finalized. Initially, this set is empty.
2) Assign a distance value to all vertices in the input graph. Initialize all distance values as INFINITE. Assign distance value as 0 for the source vertex so that it is picked first.
3) While sptSet doesn’t include all vertices
….a) Pick a vertex u which is not there in sptSet and has minimum distance value.
….b) Include u to sptSet.
….c) Update distance value of all adjacent vertices of u. To update the distance values, iterate through all adjacent vertices. For every adjacent vertex v, if sum of distance value of u (from source) and weight of edge u-v, is less than the distance value of v, then update the distance value of v
"""

import sys



class Graph:
    
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0]*self.V for row in xrange(self.V)]
    
    def minDistance(self, dist, sptSet):
        min = sys.maxint
        # heap can be used for  finding min
        for v in xrange(len(dist)):
            if min >= dist[v]  and sptSet[v] == False:
                min = dist[v]
                min_idx = v
                
        return min_idx
    
    
    def dijkstra(self,src):
        
        parent = [None]*self.V
        dist = [sys.maxint]*self.V
        sptSet = [False] *self.V
        
        
        dist[src] = 0
        
        for count in xrange(self.V):    
            u = self.minDistance(dist, sptSet)
            sptSet[u] = True
            
            for v in xrange(self.V):
                if self.graph[u][v] > 0 and sptSet[v] == False and dist[u] + self.graph[u][v] <  dist[v]:
                    dist[v] = dist[u] + self.graph[u][v]
                    parent[v] = u
                    
        self.printDijkstra(src, dist, parent)

    def printDijkstra(self, src, dist, parent):
        
        for v in xrange(len(dist)):
            if v != src: 
                print(str(parent[v]) + " ----  " + str(v) + " =  " + str(dist[v]))
            

if __name__ == "__main__":
    g  = Graph(9)
    g.graph = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
           [4, 0, 8, 0, 0, 0, 0, 11, 0],
           [0, 8, 0, 7, 0, 4, 0, 0, 2],
           [0, 0, 7, 0, 9, 14, 0, 0, 0],
           [0, 0, 0, 9, 0, 10, 0, 0, 0],
           [0, 0, 4, 14, 10, 0, 2, 0, 0],
           [0, 0, 0, 0, 0, 2, 0, 1, 6],
           [8, 11, 0, 0, 0, 0, 1, 0, 7],
           [0, 0, 2, 0, 0, 0, 6, 7, 0]
          ];
 
    g.dijkstra(0) #src is 0