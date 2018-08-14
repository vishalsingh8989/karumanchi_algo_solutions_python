

def findPair(n):
    
    dp = [0 for i in xrange(n+1)]
    
    dp[0] = 1
    
    for i in xrange(n+1):
        if i <=  2:
            dp[i] = i
        else:
            dp[i] = dp[i-1] + (i-1)*dp[i-2]
    
    return dp[n]



if __name__ == "__main__":
    
    n = 4
    print(findPair(n))
    