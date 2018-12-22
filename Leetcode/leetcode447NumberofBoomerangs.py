import math
class Solution(object):
    def numberOfBoomerangs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        
        def fact(n): 
            
            if n == 0 or n <  0:
                return 1
            if n == 1:
                return 1
            return n * fact(n-1)
        
        
        def distance(point_a, point_b):
            return math.sqrt((point_a[0] - point_b[0])**2  + (point_a[1] - point_b[1])**2 )
        
        
        def permute(val, num):
            return fact(val)/fact(val-num)
        
        result = 0
        for i in xrange(len(points)):
            count = {}
            for j in xrange(len(points)):
                if i != j:
                    print(i,j)
                    dist = distance(points[i], points[j])
                    count[dist] = count.get(dist, 0)+1
            
            for key , val in count.iteritems():
                if val != 1:
                    
                    result +=  permute(val, 2)
        return result


if __name__ == "__main__":
    sol = Solution()
    
    points = [[0,0],[1,0],[2,0]]
    sol.numberOfBoomerangs(points)
            