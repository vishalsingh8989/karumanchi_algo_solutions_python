def test(nums):
    res =  all(nums[i] <= nums[i+1] for i in xrange(len(nums)-1))
    if res is False :
        return False
    else:
        return True