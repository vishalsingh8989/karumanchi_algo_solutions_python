"""

Given a room with thief on left side of the room with finite number of sensors.
 He has to reach on right side missing the sensors. Each sensor is placed at any 
 random point in the room and has its coverage in the radius r. Find out if the thief 
 can reach to the right side without touching the range of any sensor.? 

"""


# Assume all sensors are within a room, the actual width of the room does not matter.
def canGoFromLeftToRight(roomHeight, sensors, r):
    ids = range(len(sensors))

    def union(i,j):
        ids[find(i)] = find(j)

    def find(i):
        while (i != ids[i]):
            ids[i] = ids[ids[i]]
            i = ids[i]
        return i

    top = []
    bottom = []
    
    for i,[x,y] in enumerate(sensors):
        if y+r >= roomHeight: # overlaps top side of the room
            top += [i]
        if y <= r: # overlaps bottom side of the room
            bottom += [i]

    if not top or not bottom:
        return True

    # unite all sensors overlapping the top
    for i,j in zip(top, top[1:]):
        union(j,i)

    # unite all sensors overlapping the bottom
    for i,j in zip(bottom, bottom[1:]):
        union(i,j)

    # unite all sensors overlapping each other
    for i,[x,y] in enumerate(sensors):
        for I,[X,Y] in enumerate(sensors[i+1:],i+1):
            if (X-x)*(X-x) + (Y-y)*(Y-y) <= r*r:
                union(i,I)

    # top sensor and bottom sensor not in same subset thats means 
    # there must be some path between the subsets
    return find(top[0]) != find(bottom[0])

res = canGoFromLeftToRight(1, [(0,0),(0.5,0.2),(0.7,0.4),(0.6,0.6),(1,1)], 0.5) # False
print(res)
res = canGoFromLeftToRight(1, [(0,0),(0.5,0.2),(0.7,0.4),(1,1)], 0.5) # True
print(res)

