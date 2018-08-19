def longestPallindromeSubSeqRec(string, i, j):
    if i == j:
        return 1
    elif string[i] == string[j]  and i+1 == j:
        return 2
    elif string[i] == string[j]:
        return longestPallindromeSubSeqRec(string, i+1, j-1) + 2 
    else:
        return max(longestPallindromeSubSeqRec(string, i+1, j), longestPallindromeSubSeqRec(string, i, j-1))


def longestPallindromeSubSeqDp(string):
    n = len(string)
    
    dp = [ [0]*(n) for _ in xrange(n)]
    
    for i in xrange(n):
        dp[i][i] = 1
    
    for length in xrange(2, n+1):
        for i in xrange(n - length + 1):
            j = i + length - 1
            if string[i] == string[j] and length == 2:
                dp[i][j] = 2
            elif string[i] == string[j]:
                dp[i][j] = dp[i+1][j-1] + 2
            else:
                dp[i][j] = max(dp[i+1][j], dp[i][j-1])
      
    s = 0
    
    for row in dp:
        s +=  sum(row)
        
    print("Sum : " , s)          
    return dp[0][n-1]

if __name__ == "__main__":
    string = "GEEKSFORGEEKS"
    print(longestPallindromeSubSeqRec(string, 0, len(string)-1), longestPallindromeSubSeqDp(string))
    
    
    