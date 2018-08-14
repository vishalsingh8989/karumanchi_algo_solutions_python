

def maximumArea(histogram):
    
    stack = []
    
    max_area = -1
    i = 0
    size = len(histogram)
    
    for i in xrange(len(histogram)):
        if  not stack or histogram[stack[-1]] <= histogram[i]:
            stack.append(i)
        else:
            while stack and histogram[stack[-1]]  > histogram[i]:
                j = stack.pop()
                if stack:
                    area_so_far = histogram[j] *(i - stack[-1] - 1)
                else:
                    area_so_far = histogram[j]* i
                max_area = max(area_so_far, max_area)
            stack.append(i)
            
    while stack:
        j = stack.pop()
        if stack:
            area_so_far = histogram[j] * (i - stack[-1] - 1)
        else:
            area_so_far = histogram[j] * (i)
        max_area = max(max_area, area_so_far)
    
        
    return max_area     



if __name__ == "__main__":
    histogram = [6, 2, 5, 4, 5, 1, 6]
    area = maximumArea(histogram)
    print(area)