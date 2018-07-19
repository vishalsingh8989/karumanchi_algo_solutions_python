
""" 
From list of string find longest common prefix
"""

def allcontainmid(strs, start, end, string):
    for i in xrange(len(strs)):
        for j in xrange(start,end):
            if strs[i][j] != string[j]:
                return False
    return True
            
            
         

def findlongCommonPrefix(strs):
    
    lens = [len(s) for s in strs]
    min_size = min(lens)
    
    
    l, h = 0 ,  min_size
    prefix = ""
    while l <=h:

        m = l + (h - l)/2

        if allcontainmid(strs, l , m, strs[0]):
            prefix = prefix + strs[0][l:m-l+1]
            l = m + 1
        else:
            h = m - 1
    print(prefix)
    return m


if __name__ == "__main__":
    strs = ["geeksforgeeks", "geeks",
                    "geek", "geezer"]
    #strs = ["aa" , "aabc" , "aabdf"]
    res = findlongCommonPrefix(strs)
    print(res)