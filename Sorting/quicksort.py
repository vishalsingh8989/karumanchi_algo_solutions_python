

from sorttest import test
import random
import time





def partition(nums, low, high):
    pivot  = low
    #pivot  = random.randint(low, high)
    i = low
    j = high
    
    
    while True:
        
        while i <= high and nums[i] <= nums[pivot]:
            i += 1
        
        while j >= 0 and nums[j] > nums[pivot]:
            j -=1
        
        if i >= j:
            break
        
        nums[i], nums[j] = nums[j] , nums[i]
    
    nums[pivot] , nums[j] = nums[j], nums[pivot]
    
    return j




def quickSort(nums, low, high):
    
    if low < high:
        
        p = partition(nums, low, high)
        quickSort(nums, low, p - 1)
        quickSort(nums, p + 1, high)
        
        

if __name__ =="__main__":
    
    res = []
    start = time.time()
    for _ in xrange(100000):
        size = random.randint(10,200)
        nums = [random.randint(-100,100) for _ in xrange(size)]
        #print(nums)
        quickSort(nums, 0, len(nums) - 1)
        #print(nums)
        res.append(test(nums))
    
   
    end = time.time()
    
    print("%s Pass."%(res.count(True)))
    print("%s Fail."%(res.count(False)))
    print("Time :  %s"%(end-start))
        
        
# low
# 37.67  
# 48.67
# 35.49  
# 37.56
#  35.63


    
    

