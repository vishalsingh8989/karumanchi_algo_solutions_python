"""

https://www.geeksforgeeks.org/minimum-time-write-characters-using-insert-delete-copy-operation/
"""

def findMinTime(str_len = 0, insert_t = 1, copy_t = 1 , remove_t = 1):
    
    dp = [0]*(strlen + 1)
    dp[0] = 0
    dp[1] = 1
    
    
    for i in xrange(2, str_len + 1):
        if i%2 == 0:
            dp[i] = min(dp[i-1] + insert_t ,  dp[i/2] + copy_t)
        else:
            dp[i] = min(dp[i-1] + insert_t, dp[(i-1)/2] + copy_t + insert_t  )

    return dp[-1]

if __name__ == "__main__":
    