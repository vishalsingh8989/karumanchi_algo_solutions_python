""" Create combination of two string but preverse order of each string.
"""


def interWeave(str1, str2, str1_l, str2_l, curr):
    print(str1_l, str2_l, curr)
    if str1_l == len(str1)  and str2_l == len(str2) :
        print(curr)
        return
    
    if str1_l <  len(str1):
        
        interWeave(str1, str2, str1_l + 1, str2_l, curr + str1[str1_l])
    if str2_l <  len(str2):
        
        interWeave(str1, str2, str1_l, str2_l + 1, curr + str2[str2_l] )
        

if  __name__ == "__main__":
    str1 = "AB"
    str2 = "CD"
    interWeave(str1, str2,0, 0, "")
        