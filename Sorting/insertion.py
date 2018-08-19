
from sorttest import test
import random
import time


def insert(nums):

    size = len(nums)
    for i in xrange(1, size):
        key = nums[i]
        j = i - 1
        while j >= 0 and key <  nums[j]:
            nums[j+1] = nums[j]
            j = j - 1
        nums[j+1] = key 
    
         

if __name__ == "__main__":
    
    res = []
    start = time.time()
    for _ in xrange(1000):
        size = random.randint(1,100)
        nums = [random.randint(-10,20) for _ in xrange(size)]
        #print(nums)
        insert(nums)
        #print(nums)
        res.append(test(nums))
    
   
    end = time.time()
    print("%s Pass."%(res.count(True)))
    print("%s Fail."%(res.count(False)))
    print("Time :  %s"%(end-start))
 




