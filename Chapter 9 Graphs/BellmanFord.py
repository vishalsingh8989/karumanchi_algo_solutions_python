
from collections import defaultdict
from sys import maxint

class Graph:
    
    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(dict)
    
    def addEdge(self, u, v, w):
        self.graph[u][v] = w
        
    
    
    def isNegativeCycle(self):
        
        
        visited = [False]*self.V
        dist = [maxint]*self.V
        
        
        dist[0] = 0
        
        for i in xrange(self.V-1):
            for u in self.graph:
                for v, w in self.graph[u].iteritems():
                    if  dist[u] + w  < dist[v] :
                        dist[v] = dist[u] + w
        
        
        print(dist)
        
        for u in self.graph:
            for v, w in self.graph[u].iteritems():
                if  dist[u] + w < dist[v]:
                    print(v, dist[v],  dist[u] + w)
                    return True

        return False
    
if __name__ == "__main__":
    
    g = Graph(5)
    
    g.addEdge(0, 1, -1)
    g.addEdge(1, 2, -1)
    g.addEdge(2, 0, -1)
    
    
    print(g.graph)
    
    
    
    print(g.isNegativeCycle())
    