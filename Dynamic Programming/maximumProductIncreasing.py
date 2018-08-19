

def findProdIncreasing(nums):
    maxprod = nums[:]
    
    
    for i in xrange(1, len(nums)):
        for j in xrange(i):
            if nums[j] <  nums[i] and maxprod[i] <  maxprod[j]*nums[i]:
                maxprod[i] = maxprod[j]*nums[i]
    
    return max(maxprod)


arr = [3, 100, 4, 5, 150, 6]
n = len(arr)
print(findProdIncreasing(arr))
                


