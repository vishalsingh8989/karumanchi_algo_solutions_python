""" find bridges in a graph. similar to Cut vertices or articulation point.
"""


from collections import defaultdict

class Graph:
    
    
    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list)
        self.time = 0
    
    def addEdge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)
        
    def BUtil(self, u, visited, low, disc, parent):
        
        visited[u] = True
        low[u] = self.time
        disc[u] = self.time
        
        self.time +=1
        
        for v in self.graph[u]:
            if visited[v] is False:    
                parent[v] = u
                self.BUtil(v, visited, low, disc, parent)
                low[u] = min(low[u], low[v])
                
                if low[v] > disc[u]:
                    print("Bridges " + str(u) + " -- " + str(v))
                
            elif v  != parent[u] :
                low[u] = min(low[u], disc[v])
                
                
    def bridge(self):
        
        visited = [False]*self.V
        low = [float("inf")]*self.V
        disc = [float("inf")]*self.V
        parent = [-1]*self.V
        
        for v in xrange(self.V):
            if visited[v] is False:
                self.BUtil(v, visited, low, disc, parent)
        
if __name__ == "__main__":
    # Create a graph given in the above diagram
    g1 = Graph(5)
    g1.addEdge(1, 0)
    g1.addEdge(0, 2)
    g1.addEdge(2, 1)
    g1.addEdge(0, 3)
    g1.addEdge(3, 4)
     
      
    print "Bridges in first graph "
    g1.bridge()
     
    g2 = Graph(4)
    g2.addEdge(0, 1)
    g2.addEdge(1, 2)
    g2.addEdge(2, 3)
    print "\nBridges in second graph "
    g2.bridge()
     
      
    g3 = Graph (7)
    g3.addEdge(0, 1)
    g3.addEdge(1, 2)
    g3.addEdge(2, 0)
    g3.addEdge(1, 3)
    g3.addEdge(1, 4)
    g3.addEdge(1, 6)
    g3.addEdge(3, 5)
    g3.addEdge(4, 5)
    print "\nBridges in third graph "
    g3.bridge()               