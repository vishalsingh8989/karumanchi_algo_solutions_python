
"""
Find all combination with sum  == target . Duplicates allowed
"""
import random

res = []
def find(nums, target , start, curr):
    if target <  0:
        return
    elif target == 0:
        res.append(curr)
    else:
        for i in xrange(start, len(nums)):
            find(nums, target - nums[i], i, curr + [nums[i]])   # i not increased. Duplicates allow. Pick same nums[i] again
                


if __name__ == "__main__":
    nums = [1,2,3,4,5,6,7,8,9,10]
    target = 7
    res = []
    find(nums, target, 0, [])
    print(res)