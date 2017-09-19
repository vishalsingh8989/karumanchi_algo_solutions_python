def isSorted(a):
    if len(a)==1:
        return True
    else:
        return a[0]<=a[1] and isSorted(a[1:])


a = [1,2,3,4,5]
print(isSorted(a))
b = [3,2,1,6]
print(isSorted(b))
