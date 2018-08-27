"""
https://www.geeksforgeeks.org/count-balanced-binary-trees-height-h/
Count Balanced Binary Trees of Height h

count(h) = count(h-1)*count(h-1) + count(h-1)*count(h-2) + count(h-2)*count(h-1)
"""


def countTree(h):
    
    dp  = [0]*(h+1)
    
    
    dp[0] = 1
    dp[1] = 1
    
    
    for i in xrange(2, h+1):    
        dp[i] = dp[i-1]*dp[i-1] + dp[i-2]*dp[i-1] + dp[i-1]*dp[i-2]
    
    return dp[h]

if __name__ == "__main__":
    h = 3
    print(countTree(h))

