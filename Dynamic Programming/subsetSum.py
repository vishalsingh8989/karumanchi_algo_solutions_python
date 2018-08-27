"""

https://www.geeksforgeeks.org/subset-sum-problem-dp-25/

Given a set of non-negative integers, and a value sum, determine if there is a subset of the given set with sum equal to given sum.

Examples: set[] = {3, 34, 4, 12, 5, 2}, sum = 9
Output:  True  //There is a subset (4, 5) with sum 9.
"""

def subsetRec(nums, idx ,  target):
    """
    
    Time:  exponet
    """
    
    if target == 0:
        
        return True
    
    if idx == 0 and target != 0 :
        return False
    
    if  target - nums[idx-1] < 0:
        return subsetRec(nums, idx-1, target)
    return subsetRec(nums, idx - 1, target) or subsetRec(nums, idx - 1 , target - nums[idx-1])


def subsetDp(nums, target):
    
    
    
    # only 2 rows required actaully.  current and previous 
    # take idx  =  and use %2 to get curr and previos or switch betwwen 1,0 row 
    dp = [[False]*(target + 1) for i in xrange(len(nums)+1)]
    
    for i in xrange(len(nums)+1):
        dp[i][0] = True
    
    for i in xrange(1, len(nums)+1):
        for j in xrange(1, target+1):
            #print(i,j)
            if j - nums[i-1] < 0 :
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = dp[i-1][j] or dp[i-1][j-nums[i-1]]
    
    
    #for row in dp:
    #    print(row)
    
    
    return dp[len(nums)][target]    
        
        
        

if  __name__ == "__main__":
    nums = [3, 34, 4, 12, 5, 2]
    target = 9
    print(subsetRec(nums, len(nums), target), subsetDp(nums, target))