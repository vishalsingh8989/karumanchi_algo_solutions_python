""" 0-1 knapsack 
"""

def knapsackRec(W, wt, val, n):
    
    
    if n == 0 or W == 0:
        return 0
    
    if wt[n-1] >  W:
        return knapsackRec(W, wt, val, n-1)
    
    return max(val[n-1] + knapsackRec(W-wt[n-1], wt, val, n-1), knapsackRec(W, wt, val, n-1))

def knapsackDp(W, wt, val, n):
    
    
    
    dp = [[0]*(W+1) for _ in xrange(n+1)]
    
    for i in xrange(n+1):
        for j in xrange(W+1):
            if i == 0 or j == 0:
                dp[i][j] == 0
            elif wt[i-1] <= j:
                dp[i][j] = max(val[i-1] + dp[i-1][j - wt[i-1]] ,  dp[i-1][j])
            else:
                dp[i][j] = dp[i-1][j]
    
    return dp[-1][-1]

                
 
if __name__ == "__main__":
    val = [60, 100, 120]
    wt = [10, 20, 30]
    W = 50
    n = len(val)
    print(knapsackRec(W, wt, val, n), knapsackDp(W, wt, val, n))