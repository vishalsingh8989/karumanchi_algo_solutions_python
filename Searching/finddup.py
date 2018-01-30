""" sort the array. dup will come adj.
"""

import random, time

def heapify(nums, size, i):
    largest = i
    left_child = 2*i + 1
    right_child = 2*i + 2
    
    if left_child < size  and nums[largest] < nums[left_child]:
        largest = left_child
    if right_child < size and nums[largest] < nums[right_child]:
        largest = right_child
    
    if largest != i:
        nums[largest], nums[i] = nums[i], nums[largest]
        heapify(nums, size, largest)
    
    
def heapsort(nums):
    size = len(nums)
    for i in xrange(size, -1, -1):
        heapify(nums, size, i)
    
    for i in xrange(size - 1, 0, -1):
        nums[i], nums[0] = nums[0], nums[i]
        heapify(nums, i, 0)


if __name__ == "__main__":
    
    #test
    res = []
    start = time.time()
    for _ in xrange(1000):
        size = random.randint(3,100)
        nums = [x for x in xrange(size)]
        nums = nums + [random.randint(2,size-1)]
        
        heapsort(nums)
        
        for i in xrange(1, len(nums)):
            if nums[i-1] == nums[i]:
                dup = nums[i]
                break
        if nums.count(dup) == 2:
            res.append(True)
        else:
            print(dup, nums.count(dup), nums)
            res.append(False)

    end = time.time()
    print("%s Pass."%(res.count(True)))
    print("%s Fail."%(res.count(False)))
    print("Time :  %s"%(end-start))
              