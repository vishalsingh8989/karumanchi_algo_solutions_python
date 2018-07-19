""" find cut vertices in a graph
"""
from __future__ import print_function
from collections import defaultdict


class Graph:
    
    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list)
        self.time = 0
    
    
    def addEdge(self, u,v):
        self.graph[u].append(v)
        
        
    def APUtil(self, u, visited, low, disc, ap, parent):
        
        visited[u] = True
        low[u] = self.time
        disc[u] = self.time
        
        children = 0
        self.time +=1
        
        for v in self.graph[u]:
            if visited[v]  is False:
                parent[v] = u
                children +=1
                
                self.APUtil(v, visited, low, disc, ap, parent)
                
                low[u] = min(low[u], low[v])
                
                #if root and children greater than 1 then u is ap.
                if parent[u] == -1 and children > 1:
                    ap[u] = True
                
                # if back edge exist then low[v] will be lower in disc[u], lower value will 
                # propogate through back edge if any exist.if no back edge then 
                # low[v] will be greater because it is descendent of u
                
                if parent[u] != -1 and low[v] >=  disc[u]:
                    ap[u] = True
            elif v != parent[u]:
                low[u] = min(low[u], disc[v])
                    
            
        
        

     
    def AP(self):
        
        visited = [False]*self.V           
        ap = [False]*self.V
        low = [-1]*self.V
        disc = [-1]*self.V
        parent = [-1]*self.V
        
        
        self.APUtil(0, visited, low, disc, ap, parent)
        
        for i in xrange(self.V):
            if ap[i] is True:
                print(i ,end =  " ")

if __name__ == "__main__":
    g1 = Graph(5)
    g1.addEdge(1, 0)
    g1.addEdge(0, 2)
    g1.addEdge(2, 1)
    g1.addEdge(0, 3)
    g1.addEdge(3, 4)
      
    print ("Articulation points in first graph : ")
    g1.AP()
     
    g2 = Graph(4)
    g2.addEdge(0, 1)
    g2.addEdge(1, 2)
    g2.addEdge(2, 3)
    print ("\nArticulation points in second graph : ")
    g2.AP()
     
      
    g3 = Graph (7)
    g3.addEdge(0, 1)
    g3.addEdge(1, 2)
    g3.addEdge(2, 0)
    g3.addEdge(1, 3)
    g3.addEdge(1, 4)
    g3.addEdge(1, 6)
    g3.addEdge(3, 5)
    g3.addEdge(4, 5)
    print ("\nArticulation points in third graph : ")
    g3.AP()