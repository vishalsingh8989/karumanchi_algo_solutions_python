

def find(nums, i, target):
    """
    """
    
    print(i, target)
    if target == 0:
        return True
    if i == len(nums) and target != 0:
        return False
    
    if nums[i] > target:
        return find(nums, i+1, target)
    
    return find(nums, i + 1 , target - nums[i]) or find(nums, i + 1 , target)
    
    
if __name__ == "__main__":
    nums = [3, 34, 7, 12, 5, 2]
    target = 10
    res = find(nums, 0, target)
    print("Res  :" , res)