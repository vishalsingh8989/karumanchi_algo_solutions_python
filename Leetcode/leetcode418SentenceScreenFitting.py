class Solution(object):
    def wordsTyping(self, sentence, rows, cols):
        """
        :type sentence: List[str]
        :type rows: int
        :type cols: int
        :rtype: int
        """
        row = 0
        idx = 0
        count = 0
        while row <=  rows:
            


if __name__ == "__main__":
    sol = Solution()
#     rows = 4
#     cols = 5 
#     sentence = ["I", "had", "apple", "pie"]
#     print(sol.wordsTyping(sentence, rows, cols))
#      
#     rows = 3 
#     cols = 6
#     sentence = ["a", "bcd", "e"]
#     print(sol.wordsTyping(sentence, rows, cols))
#     
#     rows = 2
#     cols = 8
#     sentence = ["hello", "world"]
#     print(sol.wordsTyping(sentence, rows, cols))
    
    sentence = ["f","p","a"]
    rows = 8
    cols = 7
    print(sol.wordsTyping(sentence, rows, cols))
    
    
    