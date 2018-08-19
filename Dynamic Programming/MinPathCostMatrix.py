import sys

def minPath(matrix, m, n):
    if n < 0  or m < 0:
         return sys.maxint
    if n == 0 and m == 0:
        return matrix[m][n]
    else:
        return matrix[m][n] + min( minPath(matrix, m-1, n), minPath(matrix, m-1, n-1), minPath(matrix, m, n-1))
    
    
def minPathDP(matrix, m, n):
    
    for i in xrange(1, n+1):
        matrix[0][i] += matrix[0][i-1]
    
    for i in xrange(1, m+1):
        matrix[i][0] += matrix[i-1][0]
        
        
    for i  in xrange(1, m+1):
        for j in xrange(1, n+1):
            matrix[i][j] += min([matrix[i-1][j] ,  matrix[i][j-1], matrix[i-1][j-1]])
    

    return matrix[m][n]


if __name__ == "__main__":
    matrix= [ [1, 2, 3],
              [4, 8, 2],
              [1, 5, 3] 
              ]
    print(minPath(matrix, len(matrix)-1, len(matrix[0])-1))
    print(minPathDP(matrix, len(matrix)-1, len(matrix[0])-1))
    
    