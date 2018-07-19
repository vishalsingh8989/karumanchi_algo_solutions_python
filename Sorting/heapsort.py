
from sorttest import test
import random
import time


def heapfiy(nums, size, i):
    
    
    left_child = 2*i +1
    right_child = 2*i +2
    largest = i
    
    
    if left_child < size  and nums[largest] < nums[left_child]:
        largest = left_child
        
    if right_child <  size and nums[largest] <  nums[right_child]:
        largest = right_child
    
    if largest  != i:
        nums[largest] , nums[i] = nums[i] , nums[largest]
        heapfiy(nums, size, largest)
    

def heapsort(nums):
    size = len(nums)
    for i in xrange(size/2 +1, -1 , -1):
        heapfiy(nums, size, i)
    
    
    for i in xrange(size-1, -1 ,-1):
        nums[i] , nums[0] = nums[0], nums[i]
        heapfiy(nums, i, 0)
    

if __name__ == "__main__":
    
    res = []
    start = time.time()
   
    for _ in xrange(1000):
        size = random.randint(1,100)
        nums = [random.randint(-10,20) for _ in xrange(size)]
        heapsort(nums)
        #print(nums)
        res.append(test(nums))
     
     
    end = time.time()
    print("%s Pass."%(res.count(True)))
    print("%s Fail."%(res.count(False)))
    print("Time :  %s"%(end-start))