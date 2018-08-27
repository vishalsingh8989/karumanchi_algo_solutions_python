
def minJumpsRec(steps, l, h):
    if l == h :
        return 0
    
    if steps[l] == 0 :
        return float('inf')
    
    min_jumps = float('inf')
    for i in xrange(l+1, h + 1):
        if i <  l + steps[l] + 1:
            jumps = minJumpsRec(steps, i, h)
            if jumps != float('inf') and jumps + 1 < min_jumps:  
                min_jumps = jumps + 1
    return min_jumps
    


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
      'end is', minJumps(arr), minJumpOn(arr), minJumpsRec(arr, 0, len(arr)-1))
    
    
    