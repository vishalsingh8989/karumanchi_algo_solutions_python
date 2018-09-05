

def minTime(nums):
    
   
    
    incl = nums[0]
    excl = 0
    
    
    
    for i in xrange(1, len(nums)):
        
        incl_new = min(incl , excl) + nums[i]
        
        excl_new = incl
        
        
        incl = incl_new
        excl = excl_new
        
    
    return min(incl, excl)


if __name__ == "__main__":
    arr1 = [10, 5, 2, 7, 10]
    print(minTime(arr1))
    arr3 = [10, 5, 2, 4, 8, 6, 7, 10]
    print(minTime(arr3))
        
        
        