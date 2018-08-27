"""
repetition of items allowed.
"""


def knapsack(W, wt, val, n):
    
    dp = [0]*(W+1)


    for i in xrange(W+1):
        for j in wt:
            if j <= i:
                dp[i] = max(dp[i], dp[i - j] + j)
    
    
    return dp[-1] 

if __name__ == "__main__" :
    W = 10
    val = [1, 3, 2]
    wt = [5, 10, 15]
    n = len(val)
    print(knapsack(W, wt, val, n))