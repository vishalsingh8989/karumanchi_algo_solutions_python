"""
Input: amount = 5, coins = [1, 2, 5]
Output: 4
Explanation: there are four ways to make up the amount:
5=5
5=2+2+1
5=2+1+1+1
5=1+1+1+1+1

"""

def change(amount, coins):
    """
    :type amount: int
    :type coins: List[int]
    :rtype: int
    """
    
    if amount  == 0:
        return 1
    
    
    dp = [0]*(amount+1)
    
    dp[0] = 1
    
    
    for coin in coins:
        for i in xrange(coin , amount + 1):
                dp[i] = dp[i] + dp[i - coin]
    return dp[-1]


if __name__ == "__main__":
    amount = 5
    coins = [1,2,4]
    print(change(amount, coins))