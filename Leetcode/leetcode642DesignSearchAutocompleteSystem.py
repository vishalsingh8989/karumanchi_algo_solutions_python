

class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False
        self.count = 0
        self.query = None

class AutocompleteSystem(object):
    def __init__(self, sentences, times):
        self.root = TrieNode()
        self.query = ""
        for i , sentence in enumerate(sentences):
            self.addRecord(sentence, times[i])
        
    
    def addRecord(self,sentence, count):
        """
        """
        r = self.root
        for c in sentence:
            if c not in r.children:
                r.children[c]  = TrieNode()
            r = r.children[c]    
        r.count += count
        r.isEnd = True
        r.query = sentence
    
    
    def dfsUtil(self, node):
        ret = []
        
        if node:
            if node.isEnd:
                ret.append((node.count, node.query))
            for child in node.children:
                ret.extend(self.dfsUtil(node.children[child]))
        return ret
        
    
    def search(self, query):
        r = self.root
        
        
        for c in query:
            if c in r.children:
                r = r.children[c]
            else:
                return []
        
        return self.dfsUtil(r)
    
    def input(self, c): 
        """
        """
        results = []
        if c != "#":
            self.query += c
            results =  self.search(self.query) 
        else:
            self.addRecord(self.query, 1)   
            self.query = ""
       
        results = [ hotword[1] for hotword in sorted(results, key = lambda x :x[0], reverse = True)[:3]]
        
        #print(results)
        return results
    
        
        
class AutocompleteSystem1(object):
    def __init__(self, sentences, times):
        self.root = TrieNode()
        self.keyword = ""
        for i, sentence in enumerate(sentences):
            self.addRecord(sentence, times[i])

    def addRecord(self, sentence, hot):
        p = self.root
        #print("addRecord" ,  sentence)
        for c in sentence:
            #print(c)
            if c not in p.children:
                p.children[c] = TrieNode()
            p = p.children[c]
        p.isEnd = True
        p.data = sentence
        p.rank = hot
    
    def dfs(self, root):
        ret = []
        if root:
            if root.isEnd:
                ret.append((root.rank, root.data))
            for child in root.children:
                ret.extend(self.dfs(root.children[child]))
        return ret
        
    def search(self, sentence):
        p = self.root
        for c in sentence:
            if c not in p.children:
                return []
            p = p.children[c]
        return self.dfs(p)
    
    def input(self, c):
        results = []
        if c != "#":
            self.keyword += c
            results = self.search(self.keyword)
        else:
            self.addRecord(self.keyword, 1)
            self.keyword = ""
        print([item[1] for item in sorted(results)[:3]])
        return [item[1] for item in sorted(results)[:3]]

if __name__ == "__main__":
    
    #["AutocompleteSystem","input","input","input","input"]
    #[[["i love you","island","iroman","i love leetcode"],[5,3,2,2]],["i"],[" "],["a"],["#"]]
    
    s = ["i love you","island","ironman","i love leetcode", "My Name is Vishal", "ilu hate you", "ironwoman", "Mahi", "i love Megan"]
    t = [5,3,2,2,6,1,1,2, 3]
 
    sol = AutocompleteSystem(s, t)
    iput = "i love leetpode"
    iput = list(iput) + ["#"]
    
    
    for c in iput:
        sol.input(c)
    
    iput = "i love leetcode"
    iput = list(iput) + ["#"]
    for c in iput:
        sol.input(c)
        
    