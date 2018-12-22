


nums = [0,5,10,15,20,25,30]


x = -1
l = 0
h = len(nums) - 1


#left bisect tested on leetcode
while l < h:
    
    m = (l+h+1)//2
    if x < nums[m]:
        h = m - 1
    else:
        l = m  

print(l, h, x, nums[l])


#right bisect

l = 0
h = len(nums) - 1


while l < h:
    m = (l+h)//2
    
    if x <=  nums[m]:
        h = m
    else:
        l = m + 1
print(l, h, x, nums[l])
