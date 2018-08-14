def myatoi(string):
    if len(string) == 0:
        return 0
    
    i = 0
    while string[i] == ' ':
        i +=1
     
     
    sign = 1 #positive    
    if string[i] == "+":
        i +=1
    elif string[i] == "-":
        sign = -1
        i +=1
    
    ans = 0
    
    while i < len(string) and ord('0') <= ord(string[i]) <= ord('9'):
        ans = ans*10 +(ord(string[i]) - ord('0'))
        if ans > pow(2,31):
            return -pow(2,31) if sign  == -1 else pow(2,31) - 1
    
        i +=1
    return sign*ans


if __name__ =="__main__":
    print(myatoi("45"))
    print(myatoi("+45"))
    print(myatoi("-45"))
    print(myatoi("045"))
    print(myatoi("  45"))
    print(myatoi("  +45"))
    print(myatoi("  -45"))
    print(myatoi("  +045"))
    print(myatoi("  +4500"))
    print(myatoi("  45c4"))