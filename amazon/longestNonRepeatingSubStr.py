


def findlongestSubStr(string = ""):
    
    
    visited = [-1]*256
    max_len = 1
    cur_len = 1
    visited[ord(string[0])] = 0  
    prev = 0
    
    
    for i in xrange(1, len(string)):
        prev = visited[ord(string[i])]
        if prev == -1 or i - cur_len  > prev:
            cur_len +=1
        else:
            max_len = max(max_len , cur_len) 
            cur_len = i - prev
        
        visited[ord(string[i])] = i   
    
    max_len = max(max_len, cur_len)
    return max_len



if __name__ == "__main__":
    
    expression = {"abcabcbb" : 3,
                  "bbbbb":1,
                  "pwwkew":3,
                  "abcabcbb":3,
                  "geeksforgeeks":7,
                  "abs":3,
                  "helllo":3,
                  "namste":6
        }
    
    
    
    res = []
    for key , val in expression.iteritems():
        res.append(val == findlongestSubStr(key))
    
    
    print("%s Pass"%(res.count(True)))
    print("%s Fail"%(res.count(False)))