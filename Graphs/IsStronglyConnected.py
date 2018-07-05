""" Check if directed graph is strongly connected or not. In undirected graph, use one DFS to check, but in directed that wont work.
In directed graph run dfs 2 times, one on original graph, 2nd on transose graph.
"""


from collections import defaultdict
class Graph:
    
    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list)
    
    def addEdge(self, u, v):
        self.graph[u].append(v)
    
    
    def getTranspose(self):
        g =  Graph(self.V)
        
        for i in self.graph:
            for j in self.graph[i]:
                g.addEdge(j, i)
            
        return g
    
    def DfsUtil(self, visited, u):
        
        visited[u]  = True
        
        for v in self.graph[u]:
            if visited[v] is False:
                self.DfsUtil(visited, v)
    
    def isSC(self):
        
        visited = [False]*self.V
        self.DfsUtil(visited, 0)
        if any( i is False for i in visited):
            return False
        
        
        graph = self.getTranspose()
        
        visited = [False]*self.V
        graph.DfsUtil(visited, 0)
        if any( i is False for i in visited):
            return False
        
        return True
    
if __name__ == "__main__":
    g1 = Graph(5)
    g1.addEdge(0, 1)
    g1.addEdge(1, 2)
    g1.addEdge(2, 3)
    g1.addEdge(3, 0)
    g1.addEdge(2, 4)
    g1.addEdge(4, 2)
    print "Yes" if g1.isSC() else "No"
     
    g2 = Graph(4)
    g2.addEdge(0, 1)
    g2.addEdge(1, 2)
    g2.addEdge(2, 3)
    print "Yes" if g2.isSC() else "No"
        
        