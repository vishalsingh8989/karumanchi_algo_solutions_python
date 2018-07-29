"""
https://www.geeksforgeeks.org/print-next-greater-number-q-queries/
"""
import random



def test(one , two):
    
    for i in xrange(len(one)):
        if one[i] != two[i]:
            return False
    
    return True
        
def bruteForce(nums):
    nge = [-1 for _  in xrange(len(nums))]
    
    for i in xrange(len(nums)):
        for j in xrange(i, len(nums)):
            if nums[j] >  nums[i]:
                nge[i] = j
                break
    
    return nge

def nextGreaterElement(nums):
    nge = [-1 for _  in xrange(len(nums))]
    
    stack = []
    
    stack.append(0)
    for i in xrange(1, len(nums)):
        
        while stack:
            if nums[stack[-1]] < nums[i]:
                nge[stack[-1]] = i
                stack.pop()
            else:
                break    
        stack.append(i)
    
    return nge



if __name__ == "__main__":
    
    res = []
    for i in xrange(1000):
        
        size = random.randint(1, 200)
        nums = [random.randint(-100,500) for i in xrange(size)]
        nge1 = nextGreaterElement(nums)
        nge2 = bruteForce(nums)
        res.append(test(nge1, nge2))
    
    print("%s Pass."%(res.count(True)))
    print("%s Fail."%(res.count(False)))
        

