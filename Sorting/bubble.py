
import random
from sorttest import test
import time


    
def bubblesort(nums):
    length = len(nums)
    for i in xrange(length):
        for j in xrange(length):
            if nums[j] >  nums[i]:
                nums[i], nums[j] = nums[j], nums[i]
    return nums
    



if __name__ == "__main__":
    
    res = []
    start = time.time()
    
    for i in xrange(100):
        size = random.randint(2, 100)
        nums = [random.randint(-10, 1000) for _ in xrange(size)]
        #print(nums)
        nums = bubblesort(nums)
        #print(nums)
        res.append(test(nums))
   
    end = time.time()
    print("%s Pass."%(res.count(True)))
    print("%s Fail."%(res.count(False)))
    print("Time :  %s"%(end-start))
    
    
    
    
    
    
    
    