

def timeTaken(length , ins, copy, rem):
    
    
    dp = [0]*(length+1)
    
    for i in xrange(1, length+1):
        if i%2 == 0:
            dp[i] = min(dp[i-1] + ins, dp[i/2] + copy)
        
        else:
            dp[i] = min(dp[i-1] + ins, dp[(i+1)/2] + copy + rem)
    
    return dp[-1]


if __name__ == "__main__":
    ins = 1
    copy = 1
    rem = 2
    print(timeTaken(9, ins, copy, rem))