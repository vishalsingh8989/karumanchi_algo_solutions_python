

def numwaysDp(pcount ):
    
    dp = [0]*(pcount + 1)
    
    
    dp[0] = 1
    dp[2] = 1
    
    
    for i in xrange(4, pcount + 1, 2):
        for j in xrange(0, i-1, 2):
            dp[i] += dp[j]* dp[i-j-2]
    
    return dp[pcount]

if __name__ == "__main__":
    print(numwaysDp(8))