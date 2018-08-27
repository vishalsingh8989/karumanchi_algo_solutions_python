
def countPallinDroneSubSeq(string, i, j):
    
    if i > j:
        return 0
    elif i == j:
        return 1
    elif string[i] == string[j]:
        return countPallinDroneSubSeq(string, i+1, j) + countPallinDroneSubSeq(string, i, j - 1) + 1
    else:
        return countPallinDroneSubSeq(string, i+1, j) + countPallinDroneSubSeq(string, i, j - 1) - countPallinDroneSubSeq(string, i+1, j-1)

def countPallindromeSubseqDp(string):
    
    n = len(string)
    
    dp = [[0]*(n+2) for _ in xrange(n+2)]
    
    
    for i in xrange(n):
        dp[i][i] = 1
    
    for length  in xrange(2, n+1):
        for i in xrange(n):
            j = i + length - 1
            if j < n:
                if string[i] == string[j]:
                    dp[i][j] = dp[i+1][j] + dp[i][j-1] + 1
                else:
                    dp[i][j] = dp[i+1][j] + dp[i][j-1] - dp[i+1][j-1]
    
    return dp[0][n-1]
    
        

if __name__ == "__main__":
    string = "aabaa"
    print(countPallinDroneSubSeq(string, 0, len(string)-1), countPallindromeSubseqDp(string))