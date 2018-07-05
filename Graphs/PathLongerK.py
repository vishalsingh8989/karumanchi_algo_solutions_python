"""
find path longer than K length in weighted graph
technique : backtracking

"""

from collections import defaultdict

class Graph:
    
    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(dict)
    
    def addEdge(self, u, v, w):
        self.graph[u][v] = w
    
    
    def pathMoreThanK(self, src, k):
        
        visited = [False]*self.V
        visited[src] = True
        
        return self.pathMoreThanKUtil(visited, src, k)
    
    def pathMoreThanKUtil(self, visited, u, k):
        
        if k <= 0:
            return True
        
        #print(k)
        for v, w in self.graph[u].iteritems():
            if visited[v] is False:
                if w >= k:
                    return True
                
                visited[v] = True
                if self.pathMoreThanKUtil(visited, v, k-w):
                    return True
                
                visited[v] = False
        
        return False
    
if __name__ == "__main__":
    V = 9
    g = Graph(V)
 
    g.addEdge(0, 1, 4)
    g.addEdge(0, 7, 8)
    g.addEdge(1, 2, 8)
    g.addEdge(1, 7, 11)
    g.addEdge(2, 3, 7)
    g.addEdge(2, 8, 2)
    g.addEdge(2, 5, 4)
    g.addEdge(3, 4, 9)
    g.addEdge(3, 5, 14)
    g.addEdge(4, 5, 10)
    g.addEdge(5, 6, 2)
    g.addEdge(6, 7, 1)
    g.addEdge(6, 8, 6)
    g.addEdge(7, 8, 7)
 
    src = 0
    k = 62
    
    print(g.pathMoreThanK(src, k))
    print("**************")
    k = 60
    print(g.pathMoreThanK(src, k))
 
