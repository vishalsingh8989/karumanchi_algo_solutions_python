

def binarySearchRec(nums, low, high, val):
    if low <=  high :
        mid = low + (high - low)/2
        
        if val == nums[mid]:
            return mid
        elif nums[low] >= nums[high]:
            if nums[mid] < nums[low]:
                if val > nums[mid] and val <= nums[high]:
                    return binarySearchRec(nums, mid +1 , high, val)
                else:
                    return binarySearchRec(nums, low, mid - 1, val)
            else:
                if val < nums[mid] and val >= nums[low]:
                    return binarySearchRec(nums, low, mid - 1, val)
                else:
                    return binarySearchRec(nums, mid + 1, high, val)
        
        else:
            if val <  nums[mid]:
                return binarySearchRec(nums, low, mid - 1, val)
            else:
                return binarySearchRec(nums, mid + 1, high, val)
                
                
                

if __name__ == "__main__":
    res = []
    numslist = [[15,16,17,18,19,20,1,2,3,4,5,6,7,8,9],
            [5,6,7,8,1,2,3,4],
            [2,1],
            [1],
            [2,3,4,1,1]
            ]
    for nums in numslist:
    
        for x in nums:
            idx = binarySearchRec(nums, 0, len(nums)-1, x)
            if idx == nums.index(x):
                res.append(True)
            else:
                res.append(False)
                print(nums)

    print("%s Pass."%(res.count(True)))
    print("%s Fail."%(res.count(False)))
