
from sorttest import test
import random
import time


def merge(nums, l, m , r):
    
    size1 = m - l + 1
    size2 = r - m
    
    
    left = [0]*size1
    right = [0]*size2
    
    for x in xrange(0, size1):
        left[x] = nums[l+x]
    
    for x in xrange(0, size2):
        right[x] = nums[m + x + 1]
    
    i = 0
    j = 0
    k = l
    
    while i <  size1 and j < size2:
        if left[i] < right[j]:
            nums[k] = left[i]
            i +=1
            k +=1
        else:
            nums[k] = right[j]
            j +=1
            k +=1
    
    while i < size1:
        nums[k] = left[i]
        i +=1
        k +=1
    while j < size2:
        nums[k] = right[j]
        j +=1
        k +=1
        

def mergesort(nums, low, high):
    """
    """
    if low< high:
        mid = (low + (high-1))/2
        mergesort(nums, low, mid)
        mergesort(nums, mid+1, high)
        merge(nums, low, mid, high)


if __name__ == "__main__":
    
    res = []
    start = time.time()
    for _ in xrange(10000):
        size = random.randint(1,100)
        nums = [random.randint(-10,20) for _ in xrange(size)]
        mergesort(nums, 0, len(nums) - 1)
        #print(nums)
        res.append(test(nums))
    
   
    end = time.time()
    
    print("%s Pass."%(res.count(True)))
    print("%s Fail."%(res.count(False)))
    print("Time :  %s"%(end-start))
    
    
    
    
    
    
    
    