""" find min element and place at the start of unsorted list
"""

import random
from sorttest import test



def selection(nums):
    """ pick small and put in front.
    """
    
    for i in xrange(len(nums)):
        min_idx = i
        j = i+1
        while j < len(nums):
            if nums[j] <  nums[min_idx]:
                min_idx = j
            j = j + 1
        nums[i], nums[min_idx] = nums[min_idx], nums[i]
    

if __name__ =="__main__":
    res = [] 
    for i in xrange(1000):
        
        nums = [random.randint(-10, 40) for x in xrange(100)]
        select(nums)
        res.append(test(nums))
    
    print("%s Pass."%(res.count(True)))
    print("%s Fail."%(res.count(False)))
         
         
    
    
    