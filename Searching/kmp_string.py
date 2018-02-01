""" KMP algorithm for string searching
"""
def prefix_table(string):
    table = [0]*len(string)
    i = 1
    j = 0


    m = len(string)
    while i < m:
        print(i,j,table)
        if string[i] == string[j]:
            table[i] = j + 1
            i +=1
            j +=1
        elif j > 0:
            j = table[j - 1]
        else:
            table[i] = 0
            i +=1
    
    return table
        
    
if __name__ == "__main__":
    string = "ababaca"
    table = prefix_table(string)
    print(table)