


def countWaysRec(faces, dices, target):
    
    
    if dices == 1 and  0 < target <= faces:
        return 1
    if dices == 1 and target <= 0:
        return 0
    
    res = 0
    
    for i in xrange(1, faces+1):
        res += countWaysRec(faces, dices - 1, target - i)
    
    return res

def countWaysDp(faces , dices , target):
    
    
    table = [[0]*(target + 1) for _ in xrange(dices+1)]
    
    
    for i in xrange(1, min(faces ,  target) + 1):
        table[1][i] = 1   # get all same as target. only one way to get sum i
    
    
    # i == number of dices
    # j = sum
    for i in xrange(2, dices+1):
        for j in xrange(1,target+1):
            for k in xrange(1, min(j, faces+1)):
                table[i][j] += table[i-1][j-k]
    
    
    #for row in table:
    #    print(row)
    return table[dices][target]


if __name__ == "__main__":
    
    print(countWaysDp(4, 3, 5), countWaysRec(4, 3, 5))
    print(countWaysDp(6, 3, 8), countWaysRec(6, 3, 8))
    print(countWaysDp(4, 2, 1), countWaysRec(4, 2, 1))
    print(countWaysDp(4, 2, 5), countWaysRec(4, 2, 5))
    


