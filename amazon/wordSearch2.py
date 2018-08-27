class TrieNode:
    def __init__(self):
        self._next = [None]*26
        self._word = None
        
class Solution(object):
    
    def buildTrie(self, words):
        root = TrieNode()
        for word in words:
            temp = root
            for w in word:
                t = ord(w) - ord('a')
                if temp._next[t] is None:
                    temp._next[t] = TrieNode()
                temp = temp._next[t]
            temp._word = word
        return root
     
    def dfs(self, board, i, j, root, res):
        char = board[i][j]
        if char == "#"  or root._next[ord(char) - ord('a')] is None:
            return 
        root = root._next[ord(char) - ord('a')]
        if root._word is not None:
            res.append(root._word)
            root._word = None
            
        
        board[i][j] = "#"
        
        if i > 0: 
            self.dfs(board, i-1, j, root, res)
        if j > 0:
            self.dfs(board, i, j-1, root, res)
        if i < len(board) - 1:
            self.dfs(board, i + 1, j, root, res)
        if j < len(board[0]) - 1:
            self.dfs(board, i, j + 1, root, res)
        
        board[i][j] = char

    
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        
    
        root = self.buildTrie(words)
        
        res = []
        for i in xrange(len(board)):
            for j in xrange(len(board[0])):
                self.dfs(board, i, j , root, res)
        
        return res
        
        
if __name__ == "__main__":
    board = [["a","b"],["c","d"]]
    words = ["ab","cb","ad","bd","ac","ca","da","bc","db","adcb","dabc","abb","acb"]
    sol = Solution()
    print(sol.findWords(board, words))
    
    
    