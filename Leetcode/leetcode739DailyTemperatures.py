def dailyTemperatures(temperatures):
    """
    :type temperatures: List[int]
    :rtype: List[int]
    """
    
    from Queue import PriorityQueue
    
    q = PriorityQueue()
    res = [ ]
    for i in xrange(len(temperatures) - 1 , -1, -1):
        while not q.empty() and temperatures[q.queue[0][1]]  < temperatures[i]:
            q.get()
        
        if q.empty():
            res.append(0)
        else:
            res.append(q.queue[0][1] - i)
        q.put((temperatures[i], i))
    
    return res[::-1]


if __name__ == "__main__":
    temperatures = [73,74,75,71,69,72,76,73]
    print(dailyTemperatures(temperatures))