"""
"""

def findLongestRec(string1, string2, i, j):
    """
       O(2^n)
    """
    
    if i == len(string1) or j == len(string2):
        return 0
    
    if string1[i] == string2[j]:
        return 1 +  findLongestRec(string1, string2, i+1, j+1)

    return max(findLongestRec(string1, string2, i+1, j), findLongestRec(string1, string2, i, j+1))


def findLongestDp(string1, string2):
    
    """
        O(mn)
    """
    
    
    
    dp = [[0]*(len(string2)+1)  for _ in xrange(len(string1) + 1)]
    
    
    for i in xrange(len(string1) + 1):
        for j in xrange(len(string2) + 1):
            if i == 0 or j == 0:
                dp[i][j] = 0
            elif string1[i - 1] == string2[j - 1]:
                dp[i][j] = 1 + dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i-1][j] , dp[i][j-1])
    
    return dp[len(string1)][len(string2)]
    


def findLongest3dp(X, Y, Z, m, n, o):
    ''' Following steps build L[m+1][n+1][o+1] in
    bottom up fashion. Note that L[i][j][k]
    contains length of LCS of X[0..i-1] and
    Y[0..j-1] and Z[0.....k-1] '''
    
     
    L = [[[0 for i in range(o+1)] for j in range(n+1)]
         for k in range(m+1)]
 

    for i in range(m+1):
        for j in range(n+1):
            for k in range(o+1):
                if (i == 0 or j == 0 or k == 0):
                    L[i][j][k] = 0
                     
                elif (X[i-1] == Y[j-1] and
                      X[i-1] == Z[k-1]):
                    L[i][j][k] = L[i-1][j-1][k-1] + 1
 
                else:
                    L[i][j][k] = max(max(L[i-1][j][k],
                                         L[i][j-1][k]),
                                         L[i][j][k-1])
 
    # L[m][n][o] contains length of LCS for
    # X[0..n-1] and Y[0..m-1] and Z[0..o-1]
    return L[m][n][o]
 

    
if __name__ == "__main__":
    X = "AGGTAB"
    Y = "GXTXAYB"
    print(findLongestRec(X, Y, 0, 0))
    print(findLongestDp(X, Y))