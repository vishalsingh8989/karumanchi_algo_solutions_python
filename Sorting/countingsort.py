
from sorttest import test
import random
import time
from collections import defaultdict


def countDict(nums):
    
    mem = defaultdict(int)
    
    
    for i in xrange(len(nums)):
        mem[nums[i]] += 1
    
    
    i = 0
     
    while len(mem)  > 0:
        min_val = min(mem.keys())
        count = mem[min_val]
        while count > 0 :
            nums[i] = min_val
            count -= 1
            i += 1        
        del mem[min_val]
    
    return nums
        

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
    
    for _ in xrange(10000):
        size = random.randint(1,1000)
        nums = [random.randint(0,200) for _ in xrange(size)]
        countDict(nums)
        #print(nums)
        res.append(test(nums))
     
    
    end = time.time()
    print("%s Pass."%(res.count(True)))
    print("%s Fail."%(res.count(False)))
    print("Time :  %s"%(end-start))