"""

https://www.geeksforgeeks.org/count-number-of-ways-to-cover-a-distance/
"""

def numofwaysRec(steps ,  distance):
    
        if distance<0:
            return 0
        
        if distance == 0 :
            return 1
        
        res = 0
        for step in steps:
            res += numofwaysRec(steps, distance - step)
        return res


def numofwaysDp(steps, distance):
    dp = [0]*(distance + 1)
    
    
    dp[0] = 1
    for dist in xrange(distance+1):
        for step in steps:
            if dist - step >= 0:
                dp[dist] +=  dp[dist-step]
    
    return dp[distance]

if __name__ == "__main__":
    steps = [1,2,3]
    distance = 10
    print(numofwaysRec(steps, distance), numofwaysDp(steps, distance))
    