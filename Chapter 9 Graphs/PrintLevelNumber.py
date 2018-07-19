from collections import defaultdict
class Graph:
    def __init__(self, vertices):
        self.V =  vertices
        self.graph = defaultdict(list)
    
    def addEdge(self, u, v):
        self.graph[u].append(v)
    
    def printLevel(self, src):
        
        queue = []
        queue.append(src)
        queue.append("$")
        level = 0
        print("Node --- Level")
        while queue:
            u = queue.pop(0)
            if u == "$":
                if queue:
                    level += 1
                    queue.append("$")
            else:
                print(" " + str(u) +  " ------ " + str(level))
                for v in self.graph[u]:
                    queue.append(v)
                    

if __name__ ==  "__main__":
    g = Graph(11)
    g.addEdge(0, 1)
    g.addEdge(0, 2)
    g.addEdge(0, 3)
    
    g.addEdge(1, 4)
    g.addEdge(2, 5)
    g.addEdge(2, 6)
    g.addEdge(3, 7)
    
    g.addEdge(4, 8)
    g.addEdge(8, 9)
    g.addEdge(9, 10)
    
    g.printLevel(0)
    
        
        