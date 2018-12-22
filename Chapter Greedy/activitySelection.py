
def activitySelection(activities):
    """
    """
    
    activities = sorted(activities , key = lambda x : x[1])
    
    count = 1
    i = 0

    print(i)
    
    for j in xrange(1, len(activities)):
        
        if activities[j][0] >  activities[i][1]:
            count += 1
            i = j
            print(i)
             
    return count


if __name__ == "__main__":
    
    #s = [1 , 3 , 0 , 5 , 8 , 5]
    #f = [2 , 4 , 6 , 7 , 9 , 9]
    
    activities = [[8,9], [1,2],[0,6],[5,7],[5,9], [3,4]]
    
    print(activitySelection(activities))
    
    
    
    
    