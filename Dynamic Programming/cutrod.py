"""
Given a rod of length n inches and an array of prices that contains prices of all pieces of size smaller than n. 
Determine the maximum value obtainable by cutting up the rod and selling the pieces. 
For example, if length of the rod is 8 and the values of different pieces are given as following, 
then the maximum obtainable value is 22 (by cutting in two pieces of lengths 2 and 6)


length   | 1   2   3   4   5   6   7   8  
--------------------------------------------
price    | 1   5   8   9  10  17  17  20

"""


def cutRodRecursive(prices, size):
    """
    """
    if size <=0 :
        return 0
    
    maxval = -1
    for i in xrange(size):
        maxval = max(maxval, prices[i] + cutRodDp(prices, size-i-1))
    return maxval


def cutRodDp(prices, size):
    """ Dynamic programming
    """
    
    if size <=0 :
        return 0
    
    dp = [0]*(size + 1)
    
    
    for i in xrange(1, size + 1):
        maxval = -1
        for j in xrange(i):
            maxval = max(maxval ,  dp[i-j-1] + prices[j])
        dp[i] = maxval
    print(dp)
    return dp[-1]
            
    
    

if __name__ == "__main__":
    prices = arr = [1, 5, 8, 9, 10, 17, 17, 20]
    size = len(prices)
    print("Max value possible  : " ,  cutRodRecursive(prices, size), cutRodDp(prices, size))

