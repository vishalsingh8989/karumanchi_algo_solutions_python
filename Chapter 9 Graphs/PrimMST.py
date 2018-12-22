#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Algorithm
1) Create a set mstSet that keeps track of vertices already included in MST.
2) Assign a key value to all vertices in the input graph. Initialize all key values as INFINITE. Assign key value as 0 for the first vertex so that it is picked first.
3) While mstSet doesn’t include all vertices
….a) Pick a vertex u which is not there in mstSet and has minimum key value.
….b) Include u to mstSet.
….c) Update key value of all adjacent vertices of u. To update the key values, iterate through all adjacent vertices. For every adjacent vertex v, if weight of edge u-v is less than the previous key value of v, update the key value as weight of u-v

Time :  O(E log(V))

"""




import sys

class Graph:
    
    
    def __init__(self, vertices):
        self.V  = vertices
        self.graph = [ [0]*self.V  for row in range(self.V)]
        
    def minKey(self, key, mstSet):
        
        min = sys.maxint
        
        for v in xrange(len(key)):
            if min >  key[v] and mstSet[v] == False:
                min = key[v]
                min_idx = v
        return min_idx
    

    def printMst(self, key, parent):
        
        print("---Edge--- = Weight")
        for v in xrange(1, self.V):
            print(str(parent[v]) + " ---- " + str(v) + "  = " + str(key[v]))
    
    
    
    def primMST(self):
        """find MST from a graph
        """
        
        parent = [None]*self.V
        key = [sys.maxint]*self.V
        mstSet = [False] *self.V
        
        key[0] = 0
        parent[0] = -1
    
        for count in range(self.V):
            
            u = self.minKey(key, mstSet)
            
            mstSet[u] = True
            
            
            for v in xrange(self.V):
                if self.graph[u][v] > 0 and mstSet[v] == False and key[v] >  self.graph[u][v]:
                    key[v] = self.graph[u][v]
                    parent[v] = u
                    
        
        self.printMst(key, parent)
            
        
        
        
        
if __name__ == "__main__":
    g  = Graph(5)
    g.graph = [ [0, 2, 0, 6, 0],
                 [2, 0, 3, 8, 5],
                 [0, 3, 0, 0, 7],
                 [6, 8, 0, 0, 9],
                 [0, 5, 7, 9, 0],
               ]
     
    g.primMST()      


