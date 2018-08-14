"""
https://leetcode.com/problems/sliding-window-maximum/description/
239. Sliding Window Maximum.

Solution https://www.geeksforgeeks.org/sliding-window-maximum-maximum-of-all-subarrays-of-size-k/
"""


#run this on paper to understand

def slidingWindowMax(nums, k):
    dequeue = []
    res = []
    
    for i in xrange(k): 
        while dequeue and nums[i] >= nums[dequeue[-1]]:
            dequeue.pop()
        
        dequeue.append(i)
        
    
    for i in xrange(k , len(nums)):
        
        res.append(nums[dequeue[0]])
        
        #size is more than k pop front means move sliding window
        while dequeue and dequeue[0] <= i - k:
            dequeue.pop(0)
        
        while dequeue and nums[i] >=  nums[dequeue[-1]]:
            dequeue.pop()
        dequeue.append(i)
        
    res.append(nums[dequeue[0]])
    return res 
        
        
    
    
    
    
    
    
    
    

if __name__ == "__main__":
    nums = [1,3,-1,-3,5,3,6,7]
    k = 3
    
    print(slidingWindowMax(nums, k))



