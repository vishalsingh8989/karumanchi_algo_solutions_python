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
    
    # backtrack to savefind the subarray
    if dp[len(nums)][target] is False:
        return -1
    
    currSum = target
    i = len(nums)
    
    setone = []
    settwo = []
    
    while i > 0  and currSum >= 0:
        if dp[i-1][currSum] is True:
            setone.append(nums[i-1])
            i -= 1
        elif dp[i-1][currSum - nums[i-1]] is True:
            settwo.append(nums[i-1])
            currSum = currSum - nums[i-1]
            i -= 1

    allpos = []
    
    for i in xrange(target+1):
        if dp[-1][i] is True:
            allpos.append(i)
    
    
    print("Sum of all possible subset")
    print(allpos)
    return dp[len(nums)][target], settwo    
        
        
        

if  __name__ == "__main__":
    nums = [3, 1, 5, 9]
    
    target = sum(nums)
    print(subsetRec(nums, len(nums), target), subsetDp(nums, target))
    
    nums = [3, 1, 5, 12, 4,5]
    
    target = 9
    print(subsetRec(nums, len(nums), target), subsetDp(nums, target))
    
    
    nums = [2, 3, 4, 5, 6, 1]
    target = sum(nums)
    
    print(subsetRec(nums, len(nums), target), subsetDp(nums, target))
    
   