""" minimum number of coin required to mak change X
"""



def min_coins(coins, target):
    max_val = max(coins) + 1
    table = [max_val]*(target+1)
    table[0] = 0 
    
    for i in xrange(1, target+1):
        print(table)
        for j in xrange(0, len(coins)):
            if coins[j] <= i:
                if table[i] >  table[i-coins[j]]  + 1:
                    table[i] = table[i-coins[j]]  + 1
    
    #print(table)
    return table[target]


if __name__ == "__main__":
    coins = [ 1, 2, 5, 10, 20, 50, 100, 500, 1000]
    res = min_coins(coins, 15)
    print(res)
    
    