

def countPathsRec(n , m):
    if n == 1  or m == 1:
        return 1
    else:
        return countPathsRec(n-1, m)  + countPathsRec(n, m-1)


def countPathsDp(n, m):
    
    dp = [[0]*(m) for i in xrange(n)]
    
    
    for i in xrange(n):
        for j in xrange(m):
            if i == 0 or j == 0:
                dp[i][j] = 1
            else:
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
    
   
    return dp[n-1][m-1]

if __name__ == "__main__":
    n = 3
    m = 3
    print(countPathsRec(n, m), countPathsDp(n, m))