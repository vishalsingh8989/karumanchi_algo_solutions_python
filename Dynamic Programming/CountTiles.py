"""
"""

def countArragement(n , m):
    
    dp = [0]*(n+1)
    
    for i in xrange(1, n+1):
        if i > m:
            dp[i] = dp[i-1] + dp[i-m]  # arrange one tile vertically then calculate remaining  +  
                                       # arrange  tiles horizontally in m columns and calculate for i - m
        elif i < m:
            dp[i] = 1
        else:
            dp[i] = 2
    
    
    print(dp)
    return dp[n]


if __name__ == "__main__":
    n = 7   #  n X m
    m = 4   # tile 1 X m
    print(countArragement(n, m))