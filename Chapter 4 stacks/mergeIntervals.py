


def partition(intervals, l, h):
    
    i = l
    j = h
    
    pivot = i
    
    while True:
        
        while i <= h and intervals[i][0] <= intervals[pivot][0]:
            i +=1
            
        while j >= l and intervals[j][0] > intervals[pivot][0]:
            j -=1
            
        if j <= i:
            break
        
        intervals[i] , intervals[j] = intervals[j], intervals[i]
    
    
    intervals[pivot] , intervals[j] = intervals[j], intervals[pivot]
    
    return j

def QuickSort(intervals, l, h):
    if l < h:
        p = partition(intervals, l, h)
        QuickSort(intervals, l, p-1)
        QuickSort(intervals, p+1, h)
        

def mergeIntervals(intervals):
    
    res = []
    QuickSort(intervals, 0, len(intervals) - 1)
    
    
    res.append(intervals[0])
    for i in xrange(1,len(intervals)):
        if res[-1][1] >= intervals[i][0]:
            res[-1][1] = max(res[-1][1],intervals[i][1] )
        else:
            res.append(intervals[i])
        
    return res

if __name__ == "__main__":
    
    intervals =  [ [ 6,8 ] , [ 1,9 ] , [ 4,7 ] , [10,13] ,[15,17] , [23,26] , [14,19]]
    res = mergeIntervals(intervals)
    print(res)
    
    
    
    
    