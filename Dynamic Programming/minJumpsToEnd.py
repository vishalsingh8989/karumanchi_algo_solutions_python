

def minJumps(steps):
    """
    O(n^2)
    """
    
    jumps = [float('inf')]*(len(steps))
    
    
    jumps[0] = 0
    
    
    for i in xrange(len(steps)):
        for j in xrange(1, steps[i]+1):
            if  i + j <  len(steps):
                print(i,j,i+j)
                jumps[i+j] = min(jumps[i+j] ,  jumps[i] + 1)
    
    print(jumps)
    return jumps[-1]

def minJumpOn(steps):
    """
    O(n)
    """
    
    currmax = 0
    jumps = 0
    maxReach = 0
    
    
    for i in xrange(len(steps)):
        currmax = max(currmax, i+steps[i])
        if i == maxReach:
            maxReach = currmax
            jumps +=1
            if maxReach >= len(steps) - 1:
                break
    return jumps
    
    
    

if __name__ == "__main__":
    arr = [1, 3, 6, 1, 0, 9]
    print('Minimum number of jumps to reach',
      'end is', minJumps(arr), minJumpOn(arr))
    
    
    