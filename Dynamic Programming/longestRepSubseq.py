"""
https://www.geeksforgeeks.org/longest-repeated-subsequence/
"""



def findLongestRepDP(string1, string2):
    """O(mn)
    """
    
    
    dp = [[0]*(len(string1) + 1) for _ in xrange(len(string2) + 1)]
    
    
    for i in xrange(len(string2) + 1):
        for j in xrange(len(string1) + 1):
            if i ==0  or j == 0:
                dp[i][j] = 0
            elif string1[j-1] == string[i-1] and i != j:
                dp[i][j] = 1 + dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i-1][j] ,  dp[i][j-1])
    
    return dp[len(string2)][len(string1)]



if __name__ == "__main__":
    string  = "AABEBCDD"
    print(findLongestRepDP(string, string))
    