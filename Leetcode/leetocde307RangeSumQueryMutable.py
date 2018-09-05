import sys
class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        size = 2*self.nextp(len(nums)) - 1
        self.segment_tree = [0]*size
        
        self.size = len(nums)
        self.nums = nums
        self.construct(0, len(nums)-1 , 0)
        #print(self.segment_tree)

    def nextp(self, n):
        v = 1
        while v < n:
            v = v << 1
        return v
      
    
    def construct(self, low, high , pos):
        
        if pos >= len(self.segment_tree):
            return 0
        if low ==  high:
            self.segment_tree[pos] = self.nums[low]
            return self.nums[low]
        mid =  (low + high)/2
        l = self.construct(low, mid, 2*pos+1)
        r = self.construct(mid+1, high, 2*pos+2)
        self.segment_tree[pos] = l + r
        
        return self.segment_tree[pos]
        
    def updateNode(self, low, high, pos,  i , val):
        if pos >= len(self.segment_tree):
            return
        if low == high:
            self.nums[low] = val
            self.segment_tree[pos] = self.nums[low]
        else:
            mid = (low+high)/2
            
            
            if  low <=  i <= mid:
                self.updateNode(low, mid, 2*pos + 1, i, val)
            else:
                r = self.updateNode(mid+1, high, 2*pos + 2, i, val)
            
            if 2*pos+1 <  len(self.segment_tree):
                self.segment_tree[pos]  = self.segment_tree[2*pos+1]
            if 2*pos+2 <  len(self.segment_tree):
                self.segment_tree[pos]  += self.segment_tree[2*pos+2]
            
            
        
            
    
    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: void
        """
        self.updateNode(0, len(self.nums) - 1, 0, i, val)
        
    
    def query(self, low, high, pos, i ,j):
        
        if pos >=  len(self.segment_tree):
            return 0
        
        if i >  high or j < low:
            return 0
        
        if i <= low and high <= j:
            return self.segment_tree[pos]
        
        mid = (low + high)/2
        
        l = self.query(low, mid, 2*pos + 1, i, j)
        r = self.query(mid+1, high, 2*pos + 2, i, j)

        return l + r
    
    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        ret = self.query(0, len(self.nums) - 1, 0, i, j)
        #print(ret)
        return ret
        
        
        


# Your NumArray object will be instantiated and called as such:
nums = [1, 3, 5]
obj = NumArray(nums)
obj.sumRange(0, 2) #-> 9
obj.update(1, 2)
obj.sumRange(0, 2)# -> 8
#param_2 = obj.sumRange(i,j)