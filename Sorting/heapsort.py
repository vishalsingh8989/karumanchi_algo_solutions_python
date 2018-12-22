
from sorttest import test
import random
import time




def heapify(nums, length, i):
    largest = i
    
    left_child = 2*i + 1
    right_child = 2*i + 2
    
    if left_child <  length and nums[left_child] >  nums[largest]:
        largest = left_child
        
    if right_child <  length  and nums[right_child] >  nums[largest]:
        largest = right_child
    
    if i != largest:
        nums[i], nums[largest] = nums[largest],nums[i]
        heapify(nums, length, largest)
        


def heapsort(nums):
    
    length = len(nums)
    for i in xrange(length /2 + 1, -1, -1):
        heapify(nums, length, i)
    
    
    for i in xrange(length - 1, -1 , -1):
        nums[0], nums[i] = nums[i], nums[0]
        heapify(nums, i, 0)
    
    

if __name__ == "__main__":
    
    res = []
    start = time.time()
   
    for _ in xrange(100):
        size = random.randint(1,100)
        nums = [random.randint(-10,20) for _ in xrange(size)]
        heapsort(nums)
        res.append(test(nums))
     
     
    end = time.time()
    print("%s Pass."%(res.count(True)))
    print("%s Fail."%(res.count(False)))
    print("Time :  %s"%(end-start))