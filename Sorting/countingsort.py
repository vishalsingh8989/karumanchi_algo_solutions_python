
from sorttest import test
import random
import time


def countsort(nums):
     
    m = max(nums)
    count = [0]*(m+1)
 
    for i in xrange(len(nums)):
        count[nums[i]] += 1
     
    for i in xrange(1, len(count)):
        count[i] += count[i-1]
     
     
    output = [0]*len(nums)
    for i  in xrange(len(nums)):
        output[count[nums[i]] - 1] = nums[i]
        count[nums[i]] -=1
     
    for i in xrange(len(nums)):
        nums[i] = output[i]
     
    return nums

if __name__ == "__main__":
    
    res = []
    start = time.time()
   
    for _ in xrange(2000):
        size = random.randint(1,100)
        nums = [random.randint(0,200) for _ in xrange(size)]
        c(nums)
        #print(nums)
        res.append(test(nums))
     
     
    end = time.time()
    print("%s Pass."%(res.count(True)))
    print("%s Fail."%(res.count(False)))
    print("Time :  %s"%(end-start))