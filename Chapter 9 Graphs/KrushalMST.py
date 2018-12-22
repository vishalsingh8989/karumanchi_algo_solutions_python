#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Given a connected and undirected graph, a spanning tree of that graph is a subgraph that 
is a tree and connects all the vertices together. A single graph can have many different 
spanning trees. A minimum spanning tree (MST) or minimum weight spanning tree for a weighted,
connected and undirected graph is a spanning tree with weight less than or equal to the 
weight of every other spanning tree. The weight of a spanning tree is the sum of weights 
given to each edge of the spanning tree.

Below are the steps for finding MST using Kruskal’s algorithm

1. Sort all the edges in non-decreasing order of their weight.
2. Pick the smallest edge. Check if it forms a cycle with the spanning tree formed so far. If cycle is not formed, include this edge. Else, discard it.
3. Repeat step#2 until there are (V-1) edges in the spanning tree.


Time :  O(E log(n))
"""


__author__ = "Vishal Jasrotia. Stony Brook University"
__copyright__ = ""
__license__ = "GPL"
__version__ = "1.0"
__maintainer__ = "Vishal Jasrotia"
__email__ = "jasrotia.vishal@stonybrook.edu"
__status__ = ""


from _collections import defaultdict


class Graph:
    
    
    def __init__(self, vertices):
        self.V= vertices
        self.graph = defaultdict(list)
        self.weights = [] 
    
    
    def addEdge(self,u,v, w):
        self.graph[u].append([v,w])
        self.weights.append([u,v,w])
    
    def union(self, parent, x,y):
        """
        Bounded by O(log(n))
        total changes is number of vertices and everytime set size become atleast double.
        So, n*log(n)
        
        """
        
        x_set = self.find(parent, x)
        y_set = self.find(parent, y)
        parent[x_set] = y_set

    
    def find(self, parent, x):
        if parent[x] == -1:
            return x
        return self.find(parent, parent[x])
        
    
    def KruskalMST(self):
        
        parent = [-1]*self.V        
        self.weights =  sorted(self.weights,key=lambda item: item[2])
        self.mst = Graph(self.V)
        edge_count = 0
        mst_weight = 0
        for edge_det in self.weights:
            u,v, w = edge_det
            
            x = self.find(parent, u)
            y = self.find(parent, v)
            
            if x != y: # does not make cycle
                edge_count += 1
                mst_weight += w
                self.mst.addEdge(u, v, w)
                self.union(parent,x, y)
        
        
        print("Total weight of MST  " , mst_weight)
        for edge_a, adj  in self.mst.graph.iteritems():
            for edge_b , weight  in adj:
                print(str(edge_a) + " -----> " + str(edge_b) + " = " + str(weight))
                
            
                
            
                         
        
if __name__ == "__main__":
    g = Graph(7)
    g.addEdge(0, 1, 10)
    g.addEdge(0, 2, 6)
    g.addEdge(0, 3, 5)
    g.addEdge(1, 3, 15)
    g.addEdge(2, 3, 4)
    g.addEdge(3, 4, 1)
    g.addEdge(1, 4, 0)
    g.addEdge(3, 5, 30)
    g.addEdge(3, 6, 5)
    
    g.KruskalMST()
    
    
    
    