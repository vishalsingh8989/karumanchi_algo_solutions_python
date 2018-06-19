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
    if size <= 0: # if size of the rod is less than zero then no money.
        return 0

    max_val = -1 ## start from lowest     
    for i in xrange(size): #try all and pick max profit. 
        max_val = max(max_val , prices[i] + cutRodRecursive(prices, size - i - 1))
    return max_val


def cutRodDp(prices, size):
    """ Dynamic programming
    """
    if size <=0:
        return 0
    
    dp = [0] *(size + 1)
    
    for len in xrange(1, size + 1):
        max_val = -1
        for j in xrange(0, len):
            max_val = max(max_val, prices[j] + dp[len-j-1]) 
        dp[len] = max_val
    
    print(dp)
    return dp[-1]
            
    
    

if __name__ == "__main__":
    prices = arr = [1, 5, 8, 9, 10, 17, 17, 20]
    size = len(prices)
    print("Max value possible  : " ,  cutRodRecursive(prices, size), cutRodDp(prices, size))

