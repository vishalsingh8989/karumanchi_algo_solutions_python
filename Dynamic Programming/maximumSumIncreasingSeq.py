

def findMaxSumIncreasingSeq(nums):
    
    maxsum = nums[:]
    
    for i in xrange(1, len(nums)):
        for j in xrange(i):
            if nums[i] > nums[j] and maxsum[i] <  maxsum[j]  + nums[i]:
                maxsum[i] =  maxsum[j]  + nums[i]
    
    return max(maxsum)
                


if __name__ == "__main__":
    nums = [1, 101, 2, 3, 100, 4, 5]
    print(findMaxSumIncreasingSeq(nums))