"""
https://www.geeksforgeeks.org/boolean-parenthesization-problem-dp-37/

1) .Count the number of ways we can parenthesize the expression so that the value of expression evaluates to true  #stored in T table


2) .Count the number of ways we can parenthesize the expression so that the value of expression evaluates to false  #stored in F table



"""




def countWays(symbols, operators):
    
    n = len(symbols)
    
    
    F = [[0]*(n+1)  for i in xrange(n+1)]
    T = [[0]*(n+1)  for i in xrange(n+1)]
    
    for i in xrange(n):
        F[i][i] = 1 if symbols[i]  == "F" else 0
        T[i][i] = 1 if symbols[i] == "T" else 0
    
    
    for l in xrange(1, n):
        i = 0 
        for j in xrange(l + i ,  n):
           
            T[i][j] = F[i][j] = 0
            
            for k in xrange(i , j):
                
                
                tik = T[i][k] + F[i][k]
                tkj = T[k+1][j] + F[k+1][j]
                
                
                if operators[k] == "&":
                    T[i][j] +=  T[i][k] * T[k+1][j]
                    F[i][j] +=  tik*tkj - T[i][k] * T[k+1][j]
                
                if operators[k] == "|":
                    T[i][j] += tik*tkj - F[i][k]*F[k+1][j]
                    F[i][j] += F[i][k]*F[k+1][j]
                
                if operators[k] == "^":
                    T[i][j] += T[i][k]*F[k+1][j] + F[i][k]*T[k+1][j]
                    F[i][j] += F[i][k]*F[k+1][j] + T[i][k]*T[k+1][j]  
                    
            
            
            i += 1
        
    
    # number of ways false stored in F table.
    return T[0][n-1]
    
    
if __name__ == "__main__":
    symbols = "TTFTTF"
    operators = "|&^|&"
    n = len(symbols)
 
    #There are 4 ways
    #((T|T)&(F^T)), (T|(T&(F^T))), (((T|T)&F)^T) and (T|((T&F)^T))
    #cout << countParenth(symbols, operators, n);
    
    print(countWays(symbols, operators))