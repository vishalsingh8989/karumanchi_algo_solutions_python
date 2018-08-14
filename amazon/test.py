def optimalUtilization(maximumOperatingTravelDistance, 
                       forwardShippingRouteList, returnShippingRouteList):
   # WRITE YOUR CODE HERE

  # WRITE YOUR CODE HERE
    
    motd = maximumOperatingTravelDistance
    fsr = forwardShippingRouteList
    rsr = returnShippingRouteList
    
    fsrsize = len(forwardShippingRouteList)
    rsrsize = len(returnShippingRouteList)
    
    fsr.sort(key = lambda x :x[1])
    rsr.sort(key = lambda x :x[1])
    print("**********")
    print(fsr)
    print(rsr)
    
    
    
    result = []
    
    #fsr index
    l = 0 
    
    #rsr index
    r = len(returnShippingRouteList) - 1
    
    opt = -1
    
    optcount = 0
    while l < len(forwardShippingRouteList) and r >= 0:
        
        s = fsr[l][1] + rsr[r][1]
        #print(l,r, s, opt)
        if s > opt and s <= motd:
            #print("one")
            opt = s
            optcount = 0
            result[:] = []
            result.append([fsr[l][0], rsr[r][0]])
            r -= 1
        elif s > motd:
            r -= 1
        elif s < opt:
            #print("two")
            l += 1
        elif s == opt:
            result.append([fsr[l][0], rsr[r][0]])
            
            if r > 0 and rsr[i-1][0] == rsr[i][0]:
                r -=1
            else:
                
                
            r -= 1
            l += 1
    
   
    return result


res = optimalUtilization(20, 
                       [[1,8],[2,7],[3,14]],  [[1,5],[2,10],[3,14]])
print(res)


res = optimalUtilization(20, 
                       [[1,8],[2,15],[3,9 ]],  [[1,8],[2,11],[3,12]])
print(res)


res = optimalUtilization(16, 
                       [[1,8],[2,8],[3,8]],  [[1,8],[2,8],[3,8]])
print(res)