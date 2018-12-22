





def search(nums, x):
     
    if len(nums) == 0:
        return -1
    l = 0
    r = len(nums) - 1
     
    while l < r:
        m = (l+r )//2
        if nums[m] > x:
            r = m - 1
        else:
            l = m 
    if nums[l] == x:
        return l
    return -1
 
 
import random
res = []
for i in xrange(100000):
    size = random.randint(1,10000)
    nums = [random.randint]
    x = random.choice(nums)
    i = search(nums, x)
    l = nums.index(x)
    #print("*********************************")
    #print(i, l, nums)
    res.append(i == l)
print(res.count(True))
print(res.count(False))
             

        



# sort on freq and then count
# nums = [1, 3,0,4,1,6,5,4,1,5,1, 2,1,2,1,0,0]
# 
# 
# 
# from Queue import  PriorityQueue
# 
# d = {}
# queue = PriorityQueue()
# 
# for num in nums:
#     d[num] = d.get(num, 0) + 1
# 
# 
# for key, val in d.iteritems():
#     queue.put((val, key))
# 
# res = []
# while not queue.empty():
#     val, key = queue.get()
#     res = res + [key]*val
# 
# print(res)