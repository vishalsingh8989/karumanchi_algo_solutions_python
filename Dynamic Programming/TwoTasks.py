def maxtaskRec(high, low, n):
    if n <= 0:
        return 0
    
    else:
        return max(high[n-1] + maxtaskRec(high, low, n-2) , low[n-1] + maxtaskRec(high, low, n-1))


def maxtaskDp(high, low, n):
    
    table = [0]*(n+1)
    
    
    table[0] = 0
    table[1] = high[0] # high is max of high[0] and low[0]
    
    for i in xrange(2, n+1):
        table[i] = max(high[i-1] + table[i-2] , low[i-1] + table[i-1])
        
    return table[n]
        
if __name__ == "__main__":
    n = 5
    high = [3, 6, 8, 7, 6]
    low = [1, 5, 4, 5, 3]
    print(maxtaskRec(high, low, n), maxtaskDp(high, low, n))