"""
https://www.geeksforgeeks.org/counts-paths-point-reach-origin/
"""


def countRec(x, y):
    if x == 0 or y == 0:
        return 1
    else:
        return countRec(x-1, y) +  countRec(x, y-1)



def countDp(x, y):
    dp = [ [0]*(x+1) for _ in xrange(y+1) ] 
    
    
    for i in xrange(y+1):
        for j in xrange(x+1):
            if i == 0 or j == 0:
                dp[i][j] = 1
            else:
                dp[i][j] = dp[i-1][j] + dp[i][j-1]  
            
    return dp[y][x]
        
    
if __name__ == "__main__":
    x = 3 
    y = 7
    print(countRec(x, y), countDp(x, y))
        

