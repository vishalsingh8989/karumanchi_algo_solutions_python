"""
"""

import itertools
import sys

class Graph:
    
    def __init__(self, vertices):
        self.V = list(range(vertices))
        self.graph = [[]]
    
    def findMinPath(self, s):
        min_path = sys.maxint
        path = []
        vertices = self.V.remove(s)
        
        for perm in itertools.permutations(self.V):
            i = s
            curr_min = 0
            for j in perm:
                curr_min +=  self.graph[i][j]
                i = j
            curr_min  +=  self.graph[i][s]
            min_path = min(min_path, curr_min)
            if curr_min == min_path:
                path = perm
                
        
        return min_path,  [ s ] + list(path) + [s]
        

if __name__ == "__main__":
    
    g = Graph(4)
    
    g.graph = [[ 0, 10, 15, 20 ],
                       [ 10, 0, 35, 25 ],
                       [ 15, 35, 0, 30 ],
                       [ 20, 25, 30, 0 ] ]
    s = 0
    print("Min path " , g.findMinPath(s))