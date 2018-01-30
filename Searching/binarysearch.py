
import random, time
def binarysearchIter(nums,val, left, right):
    
    if left <= right:
        mid = left + (right - left)/2
        
        if nums[mid] == val:
            return mid
        elif val < nums[mid]:
            return binarysearchIter(nums, val, left, mid - 1)
        else:
            return binarysearchIter(nums, val, mid + 1, right)
        
        return -1
    

def binarysearch(nums, val):
    left, right = 0 , len(nums) - 1
    
    while left <= right:
        
        mid = left + (right - left)/2
        #print(mid)
        if nums[mid] == val:
            return mid
        elif val < nums[mid]:
            right = mid -1
        else:
            left = mid + 1
    
    if nums[mid] == val:
        return left 
    return -1



if __name__ == "__main__":
    
    res = []
    start = time.time()
    for x in xrange(10000):
        size = random.randint(4,100)
        nums = [i for i in xrange(size)]
        val = random.randint(1,size-1) 
        idx =  binarysearch(nums, val)
        if val == idx:
            res.append(True)
        else:
            res.append(False)
        #print(nums)
        
    end = time.time()
    
    print("%s Pass."%(res.count(True)))
    print("%s Fail."%(res.count(False)))
    print("Time :  %s"%(end-start))    

    res = []
    start = time.time()
    for x in xrange(10000):
        size = random.randint(4,100)
        nums = [i for i in xrange(size)]
        val = random.randint(1,size-1) 
        idx =  binarysearchIter(nums, val, 0, size-1)
        if val == idx:
            res.append(True)
        else:
            res.append(False)
        #print(nums)
        
    end = time.time()
    
    print("%s Pass."%(res.count(True)))
    print("%s Fail."%(res.count(False)))
    print("Time :  %s"%(end-start))    