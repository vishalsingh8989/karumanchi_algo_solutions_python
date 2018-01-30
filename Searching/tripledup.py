
""" XOR all number . A XOR A = 0. So XOR will give the  number which is present 3 times
"""

import random, time

def findtripledup(nums):
    a = 0
    for x in xrange(len(nums)):
        a = a^nums[x]
    
    return a
        
    
    
if __name__ == "__main__":
    
    #test
    res = []
    start = time.time()
    for _ in xrange(1000):
        size = random.randint(3,100)
        nums = [x for x in xrange(size)]
        triple_dup = random.randint(2,size-1)
        
        nums = nums*2 + [triple_dup]
        
        dup = findtripledup(nums)
        
        if nums.count(dup) == 3:
            res.append(True)
        else:
            print(dup, nums.count(dup), nums)
            res.append(False)

    end = time.time()
    print("%s Pass."%(res.count(True)))
    print("%s Fail."%(res.count(False)))
    print("Time :  %s"%(end-start))
                  