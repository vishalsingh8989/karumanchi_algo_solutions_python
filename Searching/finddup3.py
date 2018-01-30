
""" mark value at index a[i]  negative .  first negative hit is answer
"""
import random, time
def finddup(nums):
    
    for i in xrange(len(nums)):
        if nums[abs(nums[i])] <  0:
            return nums[i]
        else:
            nums[nums[i]] = -nums[nums[i]]

if __name__ == "__main__":
    
    #test
    res = []
    start = time.time()
    for _ in xrange(1000):
        size = random.randint(3,100)
        nums = [x for x in xrange(size)]
        nums = nums + [random.randint(2,size-1)]
        
        
        dup = finddup(nums)
        
        if nums.count(dup) == 1 and nums.count(-dup) == 1:
            res.append(True)
        else:
            print(dup, nums.count(dup), nums)
            res.append(False)

    end = time.time()
    print("%s Pass."%(res.count(True)))
    print("%s Fail."%(res.count(False)))
    print("Time :  %s"%(end-start))
                  