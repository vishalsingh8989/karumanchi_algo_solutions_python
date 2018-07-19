#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
https://www.geeksforgeeks.org/minimum-steps-reach-end-array-constraints/
"""


from collections import defaultdict

def minStepsToArrayEnd(nums):
    
    adj = defaultdict(list)
    
    for i in xrange(len(nums)):
        adj[nums[i]].append(i)
    
    queue = []
    
    visited  = [False]* len(nums)
    queue.append([0,0])
    
    while queue:
    
        u ,  dist = queue.pop(0)
        visited[u] = True
        
        if u == len(nums)-1:
            return dist
        
        for v in adj[nums[u]]:
            if visited[v] is False  and v != u:
                queue.append([v, dist+1])
        
     
        if u+1 < len(nums) and visited[u+1] is False:
            queue.append([u+1, dist+1])
        
        if u-1 >= 0 and visited[u-1] is False:
            queue.append([u-1, dist+1])
            
            


if __name__ == "__main__":
    nums = [0, 1, 2, 3, 4, 5, 6, 7, 5,
                 4, 3, 6, 0, 1, 2, 3, 4, 5, 7]
    
    print(minStepsToArrayEnd(nums))
    
    nums = [5, 4, 2, 5, 0]
    print(minStepsToArrayEnd(nums))
    