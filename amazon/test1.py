





lis = [[3,2], [8,7], [6,9], [3,4],[7,8]]


maxone = float("-inf")
maxoneidx = -1
maxtwo = float("-inf")
maxtwoidx = -1


for idx in xrange(len(lis)):
    if maxone <  lis[idx][0]:
        maxone = lis[idx][0]
        maxoneidx = idx
    if maxtwo <  lis[idx][1]:
        maxtwo = lis[idx][1]
        maxoneidx = idx


new_list = []
print(maxone, maxtwo)

for x, y in lis:
    if x <  maxone  and y < maxtwo:
        if x > lis[maxtwoidx][0] or y >  lis[maxoneidx][1]:
            new_list.append([x, y])
        else:
            print([x,y])
    else:
        new_list.append([x,y])



        

        

print(new_list)