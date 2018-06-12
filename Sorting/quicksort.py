

from sorttest import test
import random
import time


def partition(nums, low, high):
    """
    """
    pivot = nums[low]
    i = low
    j = high

    while True:
        
        while i < high and pivot >= nums[i]:
            i +=1
        
        while j > low and pivot < nums[j]:
            j -=1
        
        if i >= j:
            break
        
        nums[i] , nums[j] = nums[j], nums[i]
    
    nums[low], nums[j] = nums[j], nums[low]
    
    return j
        
def quicksort(nums, low, high):
    """
    """
    
    if low < high:
        p = partition(nums, low, high)
        quicksort(nums, low, p - 1)
        quicksort(nums, p + 1, high)
    
    
    

if __name__ =="__main__":
    
    res = []
    start = time.time()
    for _ in xrange(1000):
        size = random.randint(1,100)
        nums = [random.randint(-10,20) for _ in xrange(size)]
        quick(nums, 0, len(nums) - 1)
        #print(nums)
        res.append(test(nums))
    
   
    end = time.time()
    
    print("%s Pass."%(res.count(True)))
    print("%s Fail."%(res.count(False)))
    print("Time :  %s"%(end-start))
        
        
        
    
    

