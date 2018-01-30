
f = open('input.py', 'r')
nt  = f.readline()
nt = int(nt)

slist = []

while nt:
    num = map(int,f.readline().split())
    slist.append(num[1:])
    nt -=1

nc  = int(f.readline())
#print(nc)

while nc:
    action = map(int,f.readline().split())
    #print("input %s"%action)
    if   action[0] == 0:
        slist[action[1] - 1].pop()
    elif action[0] == 1:
        if action[1] != 1:
            idx = action[1] - 1
            low = 0
            high = len(slist[idx])
            mid = (low+high)/2
            num = action[2]
            while low != high and low != high-1:
                if slist[idx][mid] > num:
                    high  = mid
                else:
                    low = mid
                mid = (low+high)/2

            slist[idx].insert(low+1, num)
        else:
            slist[0].append(action[2])

    elif action[0] == 2:
        minh = min(slist[0])

        #print("stack %s"%slist)
        idx = 0
        for i in xrange(1,len(slist)):
            #print("cur stack %s"%slist[i])
            flag = False    
            for x in xrange(len(slist[i])):
                if slist[i][x] > minh:
                    minh = slist[i][x]
                    flag = True
                    break;
                    
            if flag == False:
                print("NO")
                break;
            else:
                idx = +1
        if idx == len(slist)-1:
            print("YES")
    nc -=1










