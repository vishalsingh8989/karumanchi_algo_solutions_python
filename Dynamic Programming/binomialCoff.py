def binCoeffRec(n, k):
    
    if k == 0 or n == k:
        return 1
    
    return binCoeffRec(n-1, k-1)  + binCoeffRec(n-1, k)



def binCoeff(n, k):
    
    
    coeff = [[0]*(k+1) for _ in xrange(n+1)]
    
    for i in xrange(n+1):
        for j in xrange(min(i,k)+1):
            if j == 0 or j == i:
                coeff[i][j] = 1 # C(n,0) and C(n.n) = 1
            else:
                coeff[i][j] = coeff[i-1][j-1] + coeff[i-1][j]
    
    return coeff[n][k] 
        
    

if __name__ == "__main__":
    #for i in xrange(10):
    #s    print(binCoeffRec(10, i))
    
    print(binCoeff(5,2))
    
    