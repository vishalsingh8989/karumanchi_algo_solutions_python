class Solution(object):
    def canCross(self, stones):
        """
        :type stones: List[int]
        :rtype: bool
        """
        
        dp = {} #[[0] for i in xrange(stones[-1] + 1)]
        
        print(dp)
        
        #dp[0][0] = 1
        
        dp[0] = [0]
        for stone in stones:
            
            for jump in dp.get(stone, [0]):
                if jump == -1:
                    continue
                if jump == 0 and stone != 0:
                    continue
                for i in xrange(max(1 , jump-1), jump+2):
                    
                    if i not in dp.get(i+stone, []):
                        dp[i+stone] = dp.get(i+stone, [])  + [i]
        print(dp)
        return stones[-1] in dp
    
if __name__ == "__main__":
    stones = [0,2]
    sol = Solution()
    print(sol.canCross(stones))
    
