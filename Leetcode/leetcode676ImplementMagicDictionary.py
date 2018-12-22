class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False
        self.word = None
    
    
class MagicDictionary(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()
    
    def insert(self, word):
        r  = self.root
        for char in word:
            if char not in r.children:
                r.children[char] = TrieNode()
            r = r.children[char]
        r.isWord =True
        r.word = word
        

    def buildDict(self, dict):
        """
        Build a dictionary through a list of words
        :type dict: List[str]
        :rtype: void
        """
        for word in dict:
            self.insert(word)
        
        print("Done")
    
    def dfsUtil(self, root, idx, word):
        if idx  == len(word):
            return True
        else:
            for child, val in root.children.iteritems():
                if child == word[idx]:
                    if self.dfsUtil(root.children[child], idx+1, word):
                        return True
            return False
    
    def search(self, word):
        """
        Returns if there is any word in the trie that equals to the given word after modifying exactly one character
        :type word: str
        :rtype: bool

        """
        r = self.root
        idx = 0
        flag = False
        for char in word:
            if char in r.children:
                r = r.children[char]
                idx += 1
            else:
                flag = True
                break
        if flag:
            for child, char in r.children.iteritems():
                if self.dfsUtil(r.children[child], idx+1, word):
                    return True
        return False
        


###Your MagicDictionary object will be instantiated and called as such:
obj = MagicDictionary()
obj.buildDict(["hello", "leetcode", "vishal"])
param_2 = obj.search("hhllo")
print(param_2)
print(obj.search("hhlho"))
print(obj.search("hello"))
print(obj.search("leetcoded"))
print(obj.search("leetcodh"))
print(obj.search("teetcode"))