
from Queue import PriorityQueue


def skyline(buildings):
    
    buildings = sorted(buildings , key = lambda x: x[0])
    
    queue = PriorityQueue()
    
    #queue.put((-buildings[0][2], buildings[0]))
    #queue.put((-buildings[0][2], buildings[0]))
    queue.put((-10, [-10,-10,1]))
    #queue.put((-buildings[0][2], buildings[0]))
    
    res = []
    max_h = 0
    for b in buildings:
        max_h = max(max_h ,  b[2])
        while not queue.empty() and queue.queue[0][1] < b[0]:
            curb = queue.get()
            if max_h == curb[1][2] and not queue.empty():
                res.append([curb[1][1], queue.queue[0][1][2]])
        
        #print(queue.queue)
        if queue.empty():
            res.append([b[0], b[2]])
            queue.put((-b[2],  b))
        elif -queue.queue[0][1][2] < b[2]:
            res.append([b[0], b[2]])
            queue.put((-b[2] ,  b))
        else:
            queue.put((-b[2] ,  b))
    
    return res
    
    


if __name__ == "__main__":
    buildings  = [[2, 9, 10], [3, 7, 15], [5, 12, 12], [15, 20, 10], [19, 24, 8] ] 
    
    print(skyline(buildings))