def findMax(goldmine):
    
    rows = len(goldmine)
    cols = len(goldmine[0])
    
    
    for j in xrange(cols - 2 , -1, -1):
        for i in xrange(rows):
            #print(i ,j)
            right_up = 0 if i == 0 else goldmine[i-1][j+1]
            right_right = goldmine[i][j+1]
            right_down = 0  if i == rows - 1 else goldmine[i+1][j+1]
            
            goldmine[i][j] +=  max(right_up, right_right, right_down)
    
    #for row in goldmine:
    #    print(row)
        
    print(max(goldmine[i][0] for i in xrange(rows)))


if __name__ == "__main__":
    goldmine = [[1, 3, 3],
                   [2, 1, 4],
                  [0, 6, 4]]
    findMax(goldmine)
            
        
    goldmine = [[10, 33, 13, 15],
                  [22, 21, 04, 1],
                  [5, 0, 2, 3],
                  [0, 6, 14, 2]]
    
    findMax(goldmine)
    