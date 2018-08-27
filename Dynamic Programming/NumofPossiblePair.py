"""
"""

def pairsRec(x):
    
    if  x == 0 or x == 1:
        return 1
    
    else:
        # 1 ) Not pair with anyone and reduce the problem to x-1
        # 2) Pair with anyone from x-1 candidate and priblem reduces to x-2
        #
        #
        return pairsRec(x-1) + (x-1)*pairsRec(x-2)


def pairsDp(x):
    
    dp = [0]*(x+1)
    
    dp[0] = dp[1] = 1
    
    
    for i in xrange(2,x+1):
        dp[i] = dp[i-1] + (i-1)*dp[i-2]
    
    return dp[x]

if __name__ == "__main__":
    x = 4
    print(pairsRec(x), pairsDp(x))