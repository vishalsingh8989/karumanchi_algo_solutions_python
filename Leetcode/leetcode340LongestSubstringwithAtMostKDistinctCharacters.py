
class Solution(object):
    def lengthOfLongestSubstringKDistinct(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        counter = {}
        
        ans_i = 0
        ans_j = 0
        
        i = 0
        j = 0
        
        while j < len(s):
            while j <  len(s) and len(counter) <= k  :
                counter[s[j]]  = counter.get(s[j] , 0) + 1
                j += 1
                
            
            
            if  ans_i == 0 or  (ans_j  - ans_i <  j - i):
                
                    
                ans_j, ans_i = j , i
                if j == len(s):
                    ans_j = ans_j -1
                    break
            
            while i <= j and len(counter) > k:
                counter[s[i]] -= 1
                if counter.get(s[i], 0) == 0:
                    counter.pop(s[i])
                i += 1
        

        print(ans_i, ans_j)
        return ans_j  - ans_i 


if __name__ == "__main__":
    sol = Solution()
    
    s = "ab"
    k = 1
    res = sol.lengthOfLongestSubstringKDistinct(s, k)
    print(res)
    
    s = "aac"
    k = 2
    res = sol.lengthOfLongestSubstringKDistinct(s, k)
    print(res)
 
    s = "eceba"
    k = 2
    
    res = sol.lengthOfLongestSubstringKDistinct(s, k)
    print(res)
        
    s = "ecebaababa"
    k= 3
       
    res = sol.lengthOfLongestSubstringKDistinct(s, k)
    print(res)
      
    s = "abghfdecdefghijklabcdadrewse"
    k = 7
    res = sol.lengthOfLongestSubstringKDistinct(s, k)
    print(res)
#     

    