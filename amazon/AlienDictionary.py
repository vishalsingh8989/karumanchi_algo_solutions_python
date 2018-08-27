class Solution(object):
    def alienOrder(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        graph = {}
        indegree = {}
        
        
        for word in words:
            for w in word:
                indegree[w] = 0
        
        
        
        for i in xrange(len(words)-1):
            curr = words[i]
            nex = words[i+1]
            if curr == "rftt":
                print(curr, nex)
            l = min(len(curr), len(nex))
            for j in xrange(l):
                
                if curr[j] != nex[j]:
                    if nex[j] not in graph.get(curr[j], []):
                        graph[curr[j]] = graph.get(curr[j], []) + [ nex[j] ]
                        indegree[nex[j]] +=   1
                break
                
                    
            
        
        print(graph)
        print(indegree)
        
        
        queue = []
        count = len(indegree)  # number of vertices
        #print(count)
        
        for key, val in indegree.iteritems():
            if val == 0:
                queue.append(key)
        
        res = ""
        while queue:
            u = queue.pop(0)
            res += u
            for v in graph.get(u, []):
                indegree[v] -= 1
                if indegree[v] == 0:
                    queue.append(v)
            count -= 1 
        
        print(count, res)
        print("************************")
        if count != 0 :
            return ""
        
        return res
                
                
if __name__ == "__main__":
    
    words = ["wrt","wrf","er","ett","rftt"]
    sol = Solution()
    
    print(sol.alienOrder(words))
    words = ["wrt","wrf","er","ett","rftt", "te"]
    print(sol.alienOrder(words))
    
    