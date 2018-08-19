

from sorttest import test
import random
import time





def partition(nums,  low, high):
    
    
    pivot = nums[low]
    i = low
    j = high
    
    while True:
        while i < high and nums[i] <= pivot:
            i += 1
        
        while j >= 0 and nums[j] >  pivot:
            j -= 1
        
        if i >= j:
            break
        nums[i], nums[j] = nums[j], nums[i]
    
    
    nums[low], nums[j] = nums[j], nums[low]

    return j
    
def quickSort(nums, low, high):
    
    if low < high:
        p = partition(nums, low, high)
        quickSort(nums, low, p-1)
        quickSort(nums, p+1, high)

if __name__ =="__main__":
    
    res = []
    start = time.time()
    for _ in xrange(1000):
        size = random.randint(1,100)
        nums = [random.randint(-10,20) for _ in xrange(size)]
        #print(nums)
        quicksort(nums, 0, len(nums) - 1)
        #print(nums)
        res.append(test(nums))
    
   
    end = time.time()
    
    print("%s Pass."%(res.count(True)))
    print("%s Fail."%(res.count(False)))
    print("Time :  %s"%(end-start))
        
        
        
    
    

