# -*- coding:utf-8 -*-
"""Kadane\’s Algorithm
"""


from sys import maxint 

def findMax(nums):
    maxsum = -maxint 
    max_so_far = 0
    start = 0
    end = 0
    s = 0
    
    for i in xrange(len(nums)):
        max_so_far +=  nums[i]
        
        if maxsum < max_so_far :
            maxsum = max_so_far
            start = s
            end = i
        
        if max_so_far < 0:
            max_so_far = 0
            s = i + 1
    
    print("MAX SUM : " , maxsum)
    print("Subarray :" , nums[start:end+1])
    print("len : ", end - start + 1)
    return maxsum , nums[start:end+1]


if __name__ == "__main__":
    
    a = [-2, -3, 4, -1, -2, 1, 5, -3]
    print(findMax(a))