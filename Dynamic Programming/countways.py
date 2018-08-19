"""
https://www.geeksforgeeks.org/count-ways-reach-nth-stair-using-step-1-2-3/


1 )count the umber of ways to reach n using 1 ,2 and 3 step
2)  number of ways to make sum n using 1, 2, 3

3) Count number of ways to cover a distance
Given a distance ‘dist, count total number of ways to cover the distance with 1, 2 and 3 steps.

"""

def countRec(n):
    if n == 0 or n == 1:
        return 1
    if n == 2:
        return 2
    val = countRec(n - 3) + countRec(n - 2) + countRec(n - 1)
   
    return val



def countDp(n):
    
    dp = [0]*(n+1)
    
    
    dp[0] = 1
    dp[1] = 1
    dp[2] = 2
    
    
    for i in xrange(3, n+1):
        dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
    
    return dp[-1]

if __name__ == "__main__":
    print("res " , countRec(4))
    print("res " , countDp(4))
    
    
    
    