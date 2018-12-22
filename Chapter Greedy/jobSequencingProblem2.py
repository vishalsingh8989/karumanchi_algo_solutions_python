from matplotlib.style.core import available


def find(parent, s):
    if parent[s] == -1:
        return s
    parent[s] = find(parent, parent[s])
    return parent[s]

def union(parent, u, v):
    x_set = find(parent, u)
    y_set = find(parent, v)
    parent[v] = x_set
        

def jobSequencing(jobs):
    """ 
     Using disjoint sets by path compression
     O(nlogn) -- > sorting
     O(n) --  for loop
    """
    
    parent = [-1]*(len(jobs))
    seq = [None]*(len(jobs))
    
    jobs = sorted(jobs, key = lambda x :x[2], reverse = True)
    for job in jobs:
        availableSlot = find(parent, job[1])
        if availableSlot != -1 and availableSlot != 0 :
            union(parent, availableSlot - 1, availableSlot)
            seq[availableSlot] = job[0]
    
    print(seq)
    
            
    
    

if __name__ == "__main__":
    jobs = [['a', 2, 100], ['b', 1, 19], ['c', 2, 27],
                   ['d', 1, 25], ['e', 3, 15]]
    print(jobSequencing(jobs))
    