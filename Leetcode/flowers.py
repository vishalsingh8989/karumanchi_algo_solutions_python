from collections import deque

class Mqueue:
    def __init__(self):
        self.queue = deque()
        self.minq = deque()
    
    def append(self, x):
        self.queue.append(x)
        while self.minq and x < self.minq[-1]:
            self.minq.pop()
        self.minq.append(x)
    
    def popleft(self):
        x = self.queue.popleft()
        if self.minq and self.minq[0] == x:
            self.minq.popleft()
        return x
        
    def min(self):
        return self.minq[0]
#     
# class MinQueue(deque):
#     def __init__(self):
#         deque.__init__(self)
#         self.mins = deque()
# 
#     def append(self, x):
#         deque.append(self, x)
#         while self.mins and x < self.mins[-1]:
#             self.mins.pop()
#         self.mins.append(x)
# 
#     def popleft(self):
#         x = deque.popleft(self)
#         if self.mins[0] == x:
#             self.mins.popleft()
#         return x
# 
#     def min(self):
#         return self.mins[0]

class Solution(object):
    def kEmptySlots(self, flowers, k):
        days = [0]*len(flowers)
        for day, position in enumerate(flowers, 1):
            days[position - 1] = day
         
         
        window = Mqueue()
        ans = len(days)
         
        for i , day in enumerate(days):
            window.append(day)
            if k <=  i  < len(days) - 1:
                window.popleft()
                if k == 0 or days[i-k] <  window.min() > days[i+1]:
                    ans = min(ans, max(days[i-k], days[i+1])) 
         
        return ans if ans <=  len(days) else -1
    
#     def kEmptySlots(self, flowers, k):
#         days = [0] * len(flowers)
#         for day, position in enumerate(flowers, 1):
#             days[position - 1] = day
#  
#         window = Mqueue()
#         ans = len(days)
#  
#         for i, day in enumerate(days):
#             window.append(day)
#             if k <= i < len(days) - 1:
#                 window.popleft()
#                 if k == 0 or days[i-k] < window.min() > days[i+1]:
#                     ans = min(ans, max(days[i-k], days[i+1]))
#  
#         return ans if ans <= len(days) else -1

if __name__ == "__main__":
    nums = [5, 4, 8, 3, 7, 2, 9, 0, 1, 6]
    sol = Solution()
    print(sol.kEmptySlots(nums, 2))
    
    nums = [5, 4, 8, 3, 7, 2, 9, 0, 1, 6]
    k = 1
    print(sol.kEmptySlots(nums, k))