

def findLongestChain(chains):
    """
    O(n^2)
    """
    chains = sorted(chains , key = lambda x:x[0])
    
    dp = [1]*(len(chains))
    parent = [-1]*(len(chains))
    
    
    for i in xrange(1, len(chains)):
        for j in xrange(i):
            if chains[j][1] <  chains[i][0]:
                dp[i] = max(dp[i], dp[j] + 1)
                parent[i] = j
    
    
    mx = max(dp)
    
    index = dp.index(mx)
    print("print chain")
    while index !=-1:
        print(chains[index])
        index = parent[index]
    #print(index)
    #print(parent)
    #print(dp)
    return max(dp)



if __name__ == "__main__":
    
    
    chains = [[ 5, 24], [15, 25], [27, 40], [50, 60]]
    print(findLongestChain(chains))
    
    
