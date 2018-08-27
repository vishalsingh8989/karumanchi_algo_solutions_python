from random import randint


def subsetRec(nums, idx , target):
    """
    Time Complexity: O(2^n) In worst case, this solution tries two possibilities (whether to include or exclude) for every element.
    """
    if target == 0:
        return True
    
    if idx == 0 and target  != 0:
        return False
    
    if target - nums[idx-1] < 0:
        return subsetRec(nums, idx-1, target)
    
    return subsetRec(nums, idx-1, target) or subsetRec(nums, idx-1, target - nums[idx-1])

def subsetDp(nums, target):
    
    table = [[False]*(target+1) for i in xrange(len(nums) + 1)]
    
    
    for i in xrange(len(nums) + 1):
        table[i][0] = True
    
    for i in xrange(1,len(nums) + 1):
        for j in xrange(1, target + 1):
            if j - nums[i-1] < 0:
                table[i][j] = table[i-1][j]
            else:
                table[i][j] = table[i-1][j] or table[i-1][j-nums[i-1]]
    
    
    return table[len(nums)][target]

    
    

if __name__ == "__main__":
    res = []
    
    for i in xrange(1000):
        size = randint(10,30)
        nums = [randint(20,600) for i in xrange(size)]
        
        if sum(nums)%2 != 0:
            continue
        
        target = sum(nums)/2
        one = subsetRec(nums, len(nums), target)
        two = subsetDp(nums, target)
        #print(one, two)
        
        res.append(one is two)
    
    print("Pass  %s"%(res.count(True)))
    print("Fail %s"%(res.count(False)))
    
    
