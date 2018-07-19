from collections import defaultdict
class Graph:
    
    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list)
    
    def addEdge(self, u,v):
        self.graph[u].append(v)

    def dfsUtil(self, visited, src):
        visited[src] = True
        for u in self.graph[src]:
            if visited[u] is False:
                self.dfsUtil(visited, u)
        
        
    def countForest(self):
        count = 0 
        
        visited = [False]*self.V
        for i in xrange(self.V):
            if visited[i] is False:
                print("start : " ,  i)
                count +=1
                self.dfsUtil(visited, i)
         
        return count   
        

if __name__ == "__main__":
    g = Graph(8)
    g.addEdge(0,1)
    g.addEdge(0, 2)
    g.addEdge(3, 4)
    g.addEdge(3, 5)
    g.addEdge(6, 7)
    print(g.countForest())