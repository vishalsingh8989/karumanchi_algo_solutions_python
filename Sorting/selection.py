""" find min element and place at the start of unsorted list
"""

import random
from sorttest import test



def selection(nums):
    """ pick small and put in front.
    """
    size = len(nums)
    for i in xrange(size):
        min_idx = i
        for j in xrange(i+1, size):
            if nums[min_idx] >  nums[j]:
                min_idx = j
        
        nums[i], nums[min_idx] = nums[min_idx], nums[i]

if __name__ =="__main__":
    res = [] 
    for i in xrange(1000):
        
        nums = [random.randint(-10, 40) for x in xrange(100)]
        selection(nums)
        res.append(test(nums))
    
    print("%s Pass."%(res.count(True)))
    print("%s Fail."%(res.count(False)))
         
         
    
    
    