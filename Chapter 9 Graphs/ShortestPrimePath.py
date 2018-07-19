"""
https://www.geeksforgeeks.org/shortest-path-reach-one-prime-changing-single-digit-time/
"""

from collections import defaultdict

def FindPrimes(src, dst ,n):
    
    primes = [True]*n
    p = 2
    
    while p*p <=n:
        
        if primes[p] is True:
            for i in xrange(2*p , n , p):
                primes[i] = False
        p +=1
    num_size = len(str(src))
    
    
    return  [i for i in xrange(num_size, n) if primes[i] == True and len(str(i)) ==  4] 
    


class Graph:
    
    def __init__(self):
        self.graph = defaultdict(list)
    
    
    def addEdge(self, u,v):
        self.graph[u].append(v)
    
    def isAdj(self, num1, num2):
        diff = 0
        num1 = str(num1)
        num2 = str(num2)
        
        if num1[0] != num2[0]:
            diff +=1
        if num1[1] != num2[1]:
            diff +=1
        if num1[2] != num2[2]:
            diff +=1
        if num1[2] != num2[2]:
            diff +=1
            
        return diff == 1
        
        
    def addEdge(self, u, v):
        self.graph[u].append(v)
    
    def bfs(self, src, dst):
        
        queue = []
        visited = []
        queue.append(src)
        queue.append("$")
        level = 0
        while queue:
            
            u = queue.pop(0)
            #print("adj : " ,  self.graph[u])
            #print("current : " ,  u)
            visited.append(u)
            print("curr " ,  u)
            if u == dst :
                
                return level
            if u == "$":
                if queue:
                    level +=1
                    queue.append("$")
            else:
                for v in self.graph[u]:
                    if v not in visited:
                        queue.append(v)
            
    
    def findShorttest(self, src,dst):
        m = max(src, dst)
        primes = FindPrimes(src, dst, m)
        #print("primes : " ,  primes)
        for i in xrange(len(primes)):
            for j in xrange(i+1, len(primes)):
                if self.isAdj(primes[i],primes[j]):
                    self.addEdge(primes[i],primes[j])
        #print("graph :" ,  self.graph)
        return self.bfs(src, dst)
        

if __name__ == "__main__":
    num1 = 1033
    num2 = 8179
    g = Graph()
    
    print(g.findShorttest(num1, num2))
            
        
        