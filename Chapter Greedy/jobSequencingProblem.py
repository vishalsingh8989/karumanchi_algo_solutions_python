

def jobSequencing(jobs):
    """ 
        O(n^2)
    """
    
    slots = [False]*(len(jobs))
    result = [-1]*(len(jobs))
    
    
    
    jobs = sorted(jobs , key = lambda x :x [2], reverse = True)

        
    for i in xrange(len(jobs)):
        
        for j in xrange(min(len(jobs), jobs[i][1]) - 1 ,  -1, -1):
            if slots[j] is False:
                slots[j] = True
                result[j] = jobs[i][0]
                break
    
    return slots, result


if __name__ == "__main__":
    jobs = [['a', 2, 100], ['b', 1, 19], ['c', 2, 27],
                   ['d', 1, 25], ['e', 3, 15]]
    print(jobSequencing(jobs))
    