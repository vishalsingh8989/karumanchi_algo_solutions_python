"""
"""


class Graph:
    
    def __init__(self, vertices):
        self.V = vertices 
        self.graph = [[]]
    
    def isBipartite(self, s):
        
        queue = []
        color = [-1]*self.V
        
        color[s] = 0
        queue.append(s)
        
        while queue:
            u = queue.pop(0)
            if self.graph[u][u]  == 1:
                return False
            
            for v in xrange(self.V):
                if self.graph[u][v]  == 1 and color[v] == -1:
                    color[v] = 1 -  color[u]
                    queue.append(v)
                elif self.graph[u][v] ==  1 and color[v] == color[u]:
                    return False
        
        return True

if __name__ == "__main__":
    g = Graph(4)
    g.graph = [[0, 1, 0, 1],
            [1, 0, 1, 0],
            [0, 1, 0, 1],
            [1, 0, 1, 0]
            ]
    
    print "Yes" if g.isBipartite(0) else "No"
        