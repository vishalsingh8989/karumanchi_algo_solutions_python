class Solution:
    def count(self, n):
        return (n*(n+1)/2)
    
    
    def solve(self, ratings):
        
        candies = 0
        up = 0
        down = 0
        old_slope = 0
         
        for i in xrange(1, len(ratings)):
            if ratings[i] > ratings[i - 1]:
                new_slope = 1
            elif ratings[i] < ratings[i - 1]:
                new_slope = -1
            else:
                new_slope = 0
            
            if ( old_slope > 0 and new_slope == 0 ) or (  old_slope < 0  and new_slope >= 0):
                candies += self.count(up) + self.count(down) + max(up, down)
                up = 0
                down = 0
            
            if new_slope > 0:
                up += 1
            elif new_slope < 0 :
                down += 1
            else:
                candies += 1
            
            old_slope = new_slope
            
        candies += self.count(up) + self.count(down) + ( max(up, down) + 1)
        return candies
            
                


if __name__ == "__main__":
    ratings = [2,1,0,2,3,4,2,1,2,3,4,5,4,3,2,1]
    obj = Solution()
    print(obj.solve(ratings))
    
        
        