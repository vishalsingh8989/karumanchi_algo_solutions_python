def isSorted(nums):
	for i in xrange(1, len(nums)):
		if nums[i-1] >  nums[i]:
			return False
	return True
	