

def findLongestIncreasingSeq(nums):
    """
    """
    
    dp = [1]*(len(nums))
    
    
    for i in xrange(1, len(nums)):
        for j in xrange(i):
            if nums[j] <  nums[i] and dp[i] < dp[j] + 1:
                dp[i] = dp[j] + 1
    
    
    return max(dp)



if  __name__ == "__main__":
    nums = [10, 22, 9, 33, 21, 50, 41, 60]
    print(findLongestIncreasingSeq(nums))