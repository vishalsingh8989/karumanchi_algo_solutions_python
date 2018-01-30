""" hashing
"""

import random, time
def finddup(nums):
    mem = {}
    
    for x in xrange(len(nums)):
        if nums[x] not in mem:
            mem[nums[x]] = 1
        else:
            return nums[x]

if __name__ == "__main__":
    
    #test
    res = []
    start = time.time()
    for _ in xrange(1000):
        size = random.randint(3,100)
        nums = [x for x in xrange(size)]
        nums = nums + [random.randint(2,size-1)]
        
        
        dup = finddup(nums)
        
        if nums.count(dup) == 2:
            res.append(True)
        else:
            print(dup, nums.count(dup), nums)
            res.append(False)

    end = time.time()
    print("%s Pass."%(res.count(True)))
    print("%s Fail."%(res.count(False)))
    print("Time :  %s"%(end-start))
                  