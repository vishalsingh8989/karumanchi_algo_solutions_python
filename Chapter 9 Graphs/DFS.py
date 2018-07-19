"""
"""
from __future__ import print_function
from collections import defaultdict


class Graph:
    
    def __init__(self):
        self.graph = defaultdict(list)
    
    def addEdge(self,u,v):
        self.graph[u].append(v)
    
    
    def DFSUtil(self, v, visited):
        
        visited[v] = True
        print(str(v) + " --> ", end = " ")
        for i in self.graph[v]:
            if visited[i] is False:
                self.DFSUtil(i, visited)
        
    def DFS(self, src):
        visited = [False]*len(self.graph)
        self.DFSUtil(src, visited)
    
if __name__ == "__main__":
    g = Graph()
    g.addEdge(0, 1)
    g.addEdge(0, 2)
    g.addEdge(1, 2)
    g.addEdge(2, 0)
    g.addEdge(2, 3)
    g.addEdge(3, 3)
     
    print( "Following is DFS from (starting from vertex 2)")
    g.DFS(2)
        
        