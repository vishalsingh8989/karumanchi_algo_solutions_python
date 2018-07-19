"""
Find all combination with sum  == target . Duplicates **not** allowed
"""


res = []
def find(nums, target, curr, start):
    if target < 0 :
        return
    elif target == 0:
        res.append(curr)
    else:
        picked = []
        for i in xrange(start, len(nums)):
            if nums[i] not in picked:
                picked.append(nums[i])
                find(nums, target - nums[i], curr + [nums[i]] , i + 1) # skip duplicoates by start = i + 1
        

if __name__ == "__main__":
    nums = [1,2,3,4,5,6,7,8,9,10,1,2,3,4,5,6,7]
    nums.sort()
    target = 7
    res = []
    find(nums, target, 0, [])
    print(res)