
from sorttest import test
import random
import time


def partition(nums, low, high):
    
    
    pivot = nums[low]

    i = low
    j = high
    
    while True:    
        while i <  high and nums[i] <= pivot:
            i += 1
        
        while j > low and nums[j] >  pivot:
            j -= 1
        
        if i >= j:
            break
    
        nums[i], nums[j] = nums[j], nums[i]
        
    nums[j] , nums[low] = nums[low], nums[j] 
    
    return j
 
def iterativeQuickSort(nums, low, high):
     
    stack = []
    stack.append(low)
    stack.append(high)
    
    while len(stack) > 0: 
        h = stack.pop()
        l = stack.pop()
        
        p = partition(nums, l, h)
        
        if p - 1 > l:
            stack.append(l)
            stack.append(p-1)
        if p + 1 < h:
            stack.append(p + 1)
            stack.append(h)
            
                   
if __name__ =="__main__":
    
    res = []
    start = time.time()
    for _ in xrange(10000):
        size = random.randint(1,100)
        nums = [random.randint(-10,20) for _ in xrange(size)]
        iterativeQuickSort(nums, 0, len(nums) - 1)
        #print(nums)
        res.append(test(nums))
    
   
    end = time.time()
    
    print("%s Pass."%(res.count(True)))
    print("%s Fail."%(res.count(False)))
    print("Time :  %s"%(end-start))