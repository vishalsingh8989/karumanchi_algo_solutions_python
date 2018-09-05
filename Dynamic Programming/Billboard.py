"""
https://www.geeksforgeeks.org/highway-billboard-problem/
"""


def findProfit(miles , distance,  revenue, space ):
    
    table = [0]*(miles+1)
    
    nextbb = 0 #nextbillboard position
    
    for i in xrange(miles+1):
        
        if nextbb <  len(distance):
            if distance[nextbb] != i:
                table[i] = table[i-1]
            else:
                if i <=  space: # first one
                    table[i] = max(table[i-1], revenue[nextbb])
                else:
                    table[i] = max(table[i-space-1] + revenue[nextbb] , table[i-1])
                
                nextbb += 1
            
            
        else:
            # all billboard are placed
            table[i] = table[i-1]
    
    return table[miles]


if __name__ == "__main__":
    
    space = 5
    miles = 20
    distance = [6, 7, 12, 13, 14]
    revenue = [5, 6, 5, 3, 1]
    n = len(distance)
    print(findProfit(miles, distance, revenue, space))

        
    
    
    