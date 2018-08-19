"""
Count all possible paths from top left to bottom right of a mXn matrix
The problem is to count all the possible paths from top left to bottom right of a mXn matrix with the constraints that from each cell you can either move only to right or down
"""


def countPathRec(m,n):
    
    if m == 0 or n == 0:
        return 1
    
    return countPathRec(m-1, n) + countPathRec(m, n-1)

    
def countPathDp(m,n):
    dp = [[0]*(m+1)  for _ in xrange(n+1)]
    
    for i in xrange(n+1):
        for j in xrange(m+1):
            if i == 0 or j == 0:
                dp[i][j] = 1
            else:
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
    
    return dp[n][m]    



if __name__ == "__main__":
    m = 3 
    n = 3
    
    print(countPathRec(m, n), countPathDp(m, n))
    
    


