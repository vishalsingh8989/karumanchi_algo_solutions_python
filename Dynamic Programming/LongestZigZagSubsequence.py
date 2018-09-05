

def ZigZag(nums):
    
    table = [[1]*(len(nums)) for i in xrange(2)]
    
    res = 0
    for i in xrange(1, len(nums)):
        for j in xrange(i):
            
            if nums[j] <  nums[i] and table[0][i] <  table[1][j] + 1:
                table[0][i] =  table[1][j] + 1

            if nums[j] >  nums[i] and table[1][i] <  table[0][j] + 1:
                table[1][i] = table[0][j] + 1
            
            res = max([table[0][i], table[1][i], res])
    
    return res

if __name__ == "__main__":
    nums = [10, 22, 9, 33, 49, 50, 31, 60]
    print(ZigZag(nums))
    nums = [9, 2, 5, 5, 9, 5, 5, 5, 4, 10, 7, 10, 1, 5, 1, 2, 8, 5, 2, 8]
    print(ZigZag(nums))
    
    