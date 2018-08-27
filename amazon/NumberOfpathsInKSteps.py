from collections import defaultdict
class Graph:
    
    
    def solve(self, start, end, steps, rows,cols):
        matrix = [ [[0]*cols  for i in rows] for i in xrange(steps + 1)]
        
        





cols = 4
rows = 6
graph = [[1 for i in xrange(cols)] for j in xrange(rows)]


g = Graph()
start = [0,2]
end = [3,4]
steps = 12


for row in graph:
    print(row)


