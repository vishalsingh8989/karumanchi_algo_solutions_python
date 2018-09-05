
class TrieNode:
    def __init__(self):
        self._next = [None]*26
        self._word = None
        self._query = None
        self._count = 0
        
        
class AutocompleteSystem(object):

    def __init__(self, sentences, times):
        """
        :type sentences: List[str]
        :type times: List[int]
        """
        
        self.input_query = ""
        
        self.root = TrieNode()
        idx = 0
        for query in sentences:
            self.buildTrie(query, times[idx])
            idx += 1
            
        
       
        
    def buildTrie(self, query, count ):
        root = self.root
        for word in query.split(" "):
            word_idx = ord(word[0]) - ord('a')
            if root._next[word_idx] is None:
                root._next[word_idx] = {}
            
            if root._next[word_idx].get(word, None) is None:
                root._next[word_idx][word] = TrieNode()
            
            root = root._next[word_idx][word]
            
        root._query = query
        root._count =  root._count + count

            
        
    
    def search(self, query):
        hotwords = {}
        
        temp = self.root
        word_idx  = 0
        candidate_childs = []
        query = query.split(" ")
        for word in query[:-1]:
            word_idx = ord(word[0]) - ord('a')
            if temp._next[word_idx] is not None:
                if word in temp._next[word_idx].keys():
                    temp = temp._next[word_idx][word]
                else:
                    return []
            else:
                return []
        
        cache = {}
        
        if temp is not None:
            word = query[-1]
            if len(word)  != 0: 
                word_idx = ord(word[0]) - ord('a')
                if temp._next[word_idx] is not None:
                    candidate_keys = temp._next[word_idx].keys()
                    candidate_keys = [ key for key in candidate_keys if key.startswith(word) or key == word]
                    if len(candidate_keys) == 0:
                        return []  
                    for candidate_key in candidate_keys:
                        self.dsfUtil(query, temp._next[word_idx][candidate_key], cache)
            else:
                word_idx = [ idx for idx in xrange(26) if temp._next[idx] is not None ]
                if len(word_idx) != 0 :
                    for idx in word_idx:
                        for candidate_key, node in temp._next[idx].iteritems(): 
                            self.dsfUtil(query, node, cache)
                        
                
            
            #print(candidate_childs, temp)
            
    
        autosuggest = self.filter_top(cache)
        
        
        
        return autosuggest
    
    def filter_top(self, cache):
        
        res = []
        
        keys = cache.keys()
        keys = sorted(keys)
        while len(res) <  3:
            if len(keys) == 0:
                break
            max_freq = keys.pop()
            
            hot_query = cache.pop(max_freq)
            #print("Max freq : ", max_freq, hot_query)
            if len(hot_query) > 1:
                hot_query  = sorted(hot_query)
            res.extend(hot_query[:3-len(res)])
        
        #print("res" , res)
        return res
                
            
        
    def dsfUtil(self, query, candidate, cache ):
        
        if candidate._next.count(None) == 26:
            cache[candidate._count] = cache.get(candidate._count,[]) +  [ candidate._query ]
        else: 
            valid_childs = [ idx for idx in xrange(26) if candidate._next[idx] is not None ]
            for child in valid_childs:
                for key, node in candidate._next[child].iteritems():
                    self.dsfUtil(query ,  node, cache)
        
    
    #def insert(self):
         
    def input(self, c):
        """
        :type c: str
        :rtype: List[str]
        """
        if c != "#":
            self.input_query  += c
            print(self.input_query, self.search(self.input_query))
        else:
            self.buildTrie(self.input_query, 1)
            self.input_query = ""
        

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
        
    