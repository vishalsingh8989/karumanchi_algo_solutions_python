from collections import Counter

class Solution:
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        
        t_count =  Counter(t)
        size = len(t)
        i = 0 
        ans_i = 0
        ans_j = 0
        
        for j, char in enumerate(s, 1):
            size = size - (t_count[char] > 0)
            t_count[char] -=1
            if not size:
                while i <  j  and t_count[s[i]] <  0:
                    t_count[s[i]] +=1
                    i +=1
                if not ans_j or j - i <  ans_j - ans_i:
                    ans_i , ans_j = i , j
        return s[ans_i:ans_j]


if __name__ == "__main__":
    sol = Solution()
    S = "ADOBECODEBANC"
    T = "ABC"
    print(sol.minWindow(S, T))