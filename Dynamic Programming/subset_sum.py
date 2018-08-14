

def finddDP(nums, target):
    
   
   
    dp = [ [0]*(target+1) for i in xrange(len(nums) + 1)]
    
    for i in xrange(len(nums) + 1):
        dp[i][0] = True
    
    for i in xrange(1, target+1):
        dp[0][i] = False
    
    
    for i in xrange(1,len(nums) + 1):
        for j in xrange(1, target + 1):
            if j <  nums[i-1]:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = dp[i-1][j] or dp[i-1][j - nums[i-1]]
    
    return dp[len(nums)][target]



def find(nums, i, target):
    """
    """
    
    if target == 0:
        return True
    
    elif target != 0 and i == len(nums):
        return False
    elif target < nums[i]:
        return find(nums, i+1 , target)
    
    return find(nums, i+1, target) or find(nums, i+1, target - nums[i])
    

    
    
if __name__ == "__main__":
    nums = [3,6,7,8,12,3,10]
    target = 9
    res1 = find(nums, 0, target)
    res2 = finddDP(nums, target)
    print("Res  :" , res1, res2)
    