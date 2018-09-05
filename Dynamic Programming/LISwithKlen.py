

def LISwithK(nums, k):
    
    table = [[0]*(len(nums)) for i in xrange(k)]
    
    
    for i in xrange(len(nums)):
        table[0][i]  = 1
        
    
    for l in xrange(1, k):
        for i in xrange(len(nums)):
            table[l][i] = 0
            for j in xrange(l-1, i):
                if nums[j] <  nums[i]:
                    table[l][i] +=  table[l-1][j]

    #for row in table:
    #    print(row)
    
    return sum(table[-1])

if __name__ == "__main__":
    nums = [12, 8, 11, 13, 10, 15, 14, 16, 20]
    print(LISwithK(nums,4))        
                