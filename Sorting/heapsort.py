
from sorttest import test
import random
import time


def heapify(nums, i, size):
    largest = i 
    left_child = 2*i + 1
    right_child = 2*i + 2
    
    if left_child < size and nums[largest] <  nums[left_child]:
        largest = left_child
    
    if right_child < size and nums[largest] <  nums[right_child]:
        largest = right_child
        
    
    if largest != i:
        nums[i] , nums[largest] = nums[largest], nums[i]
        heapify(nums, largest)


def heapsort(nums):
    
    for i in xrange(len(nums), -1, -1):
        heapify(nums, i)
    
    
    
    print(nums, max(nums))


if __name__ == "__main__":
    
    res = []
    start = time.time()
    nums = [random.randint(-10,20) for _ in xrange(10)]
    print(nums)
    heapsort(nums)
#     for _ in xrange(10000):
#         size = random.randint(1,100)
#         nums = [random.randint(-10,20) for _ in xrange(size)]
#         heapsort(nums)
#         #print(nums)
#         res.append(test(nums))
#     
#    
#     end = time.time()
#     print("%s Pass."%(res.count(True)))
#     print("%s Fail."%(res.count(False)))
#     print("Time :  %s"%(end-start))