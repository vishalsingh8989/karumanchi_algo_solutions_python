def permCoeffDP(n, k):
    
    
    permCoeff = [ [0]*(k+1) for _ in xrange(n+1)]
    
    for i in xrange(n+1):
        for j in xrange(k+1):
            if j == 0:
                permCoeff[i][j] = 1
            else:
                permCoeff[i][j] = j*permCoeff[i-1][j-1] + permCoeff[i-1][j]
    
    return permCoeff[n][k]



def permFast(n,k):
    
    fn = 1
    for i in xrange(1, n+1):
        fn = fn*i
        if i == n -k :
            fk = fn


    return fn/fk     
   
if __name__ == "__main__":
    print(permCoeffDP(10, 2))
    print(permFast(10,2))