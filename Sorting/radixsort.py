

from sorttest import test
import random
import time

def c(nums, exp):
    
    count = [0]*10
    
    
    for i in xrange(len(nums)):
        count[(nums[i]/exp)%10] += 1
    
    for i in xrange(1,10):
        count[i] +=  count[i-1]

    output = [0]* len(nums)
    
    for i in xrange(len(nums)-1, -1, -1):
        output[count[(nums[i]/exp)%10] - 1] = nums[i]
        count[(nums[i]/exp)%10] -=1
    
    for i in xrange(len(nums)):
        nums[i] = output[i]
    
    
def r(nums):
    m = max(nums)
    exp = 1
    while m/exp > 0:
        c(nums, exp)
        exp = exp * 10
        

def countsort(nums, exp):
    
    count = [0] *10
    
    for i in xrange(len(nums)):
        count[((nums[i])/exp)%10] +=1
    
    for i in xrange(1,len(count)):
        count[i] += count[i-1]
        
    output = [0]*(len(nums))
    for i in xrange(len(nums)-1, -1, -1):  #reverse required otherwise fail
        output[count[((nums[i])/exp)%10] - 1] = nums[i]
        count[((nums[i])/exp)%10] -=1
    
    for i in xrange(len(nums)):
        nums[i] = output[i]
    
    

def radixsort(nums):
    m = max(nums)
    
    exp = 1
    while m/exp > 0:
        countsort(nums, exp)
        exp = exp*10


if __name__ == "__main__":
    
    res = []
    start = time.time()
   
    for _ in xrange(100000):
        size = random.randint(10,200)
        nums = [random.randint(0,200) for _ in xrange(size)]
        
        r(nums)
        #print(nums)
        res.append(test(nums))
     
     
    end = time.time()
    print("%s Pass."%(res.count(True)))
    print("%s Fail."%(res.count(False)))
    print("Time :  %s"%(end-start))
    