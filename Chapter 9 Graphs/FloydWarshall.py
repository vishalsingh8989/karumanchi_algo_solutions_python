"""All pair shortest path Algorithm O(n^3)
"""

import sys 
INF = sys.maxint

class Graph:
    
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []
    
    def allPairShortestPath(self):
        
        dist = self.graph
        
        for k in xrange(self.V):
            for i in xrange(self.V):
                for j in xrange(self.V):
                    try:
                        dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
                    except:
                        print("Error " , i , j , k)
        
        for row in dist:    
            print(row)
    
if __name__ == "__main__":
    
    graph = [[0,5,INF,10],
             [INF,0,3,INF],
             [INF, INF, 0,   1],
             [INF, INF, INF, 0]
        ]
    
    
    g = Graph(4)
    g.graph = graph
    
    g.allPairShortestPath()
    