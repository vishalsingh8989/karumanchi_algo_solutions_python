
# #recursive
def permuteUniqueRec(nums , visited , curr, l, res):
    if l == len(nums) - 1:
        res.append(curr)
    else:
        for i in xrange(l , len(nums)):
            pass
            

#ITERATIVE
def permuteUnique(nums):
    ans = [[]]
    for n in nums:
        new_ans = []
        for l in ans:
            for i in xrange(len(l) + 1):
                new_ans.append(l[:i] + [n] + l[i:])
                if i< len(l) and l[i] == n: #removes duplications
                    break
        ans = new_ans
                
    
    return ans


if __name__ == "__main__":
    string = [1,2,2]
    ans = permuteUnique(string)
    print(ans)
    res = []
    permuteUniqueRec(string, 0 , len(string)-1, res)
    print(res)
    string = "hello"
    ans = permuteUnique(string)
    
    print(ans)