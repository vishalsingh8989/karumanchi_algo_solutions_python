
import random
from sorttest import test
import time


    
def bubbleSort(nums):  
    size = len(nums)
    for i in xrange(size):
        for j in xrange(i+1, size):
            if nums[i]  >  nums[j]:
                nums[i], nums[j] = nums[j],nums[i]




if __name__ == "__main__":
    
    res = []
    start = time.time()
    for _ in xrange(1000):
        size = random.randint(1,100)
        nums = [random.randint(-10,20) for _ in xrange(size)]
        bubbleSort(nums)
        #print(nums)
        res.append(test(nums))
    
   
    end = time.time()
    print("%s Pass."%(res.count(True)))
    print("%s Fail."%(res.count(False)))
    print("Time :  %s"%(end-start))
    
    
    
    
    
    
    
    