def printrecursive_reverse(num, end):
    if num == end:
        print(num)
    else:
        print(num)
        printrecursive_reverse(num-1, end)



if __name__ == "__main__":
    printrecursive_reverse(10, 0)






