""" given an array. waf w
"""

import sys
sys.path.append('..')

from Sorting.sorttest import test
import random


def dutchflag(nums, low, high):
    i, j = low, high
    
    while i <  j:
        while nums[i]%2 == 0 and i < j:
            i +=1
        while nums[j]%2 == 1 and i< j:
            j -=1
        
        nums[i], nums[j] = nums[j], nums[i]
    
    
if __name__ == "__main__":
    res = []
    for x in xrange(10000):
        size = random.randint(2,50)
        nums = [random.randint(0,1) for _ in xrange(size)]
        dutchflag(nums, 0, len(nums)-1)
        res.append(test(nums))
    
    print("%s Pass."%(res.count(True)))
    print("%s Fail."%(res.count(False)))



