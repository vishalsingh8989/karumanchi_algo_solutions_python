from __future__ import print_function


def fraction(nr, dr):
    
    if nr%dr == 0:
        print(" + " + str(nr/dr), end = " ")
        return 
    
    if dr%nr == 0:
        print("+ 1/" + str(dr/nr), end = " ")
        return
    
    #if nr > dr:
    #    print("1 + ", end = " ")

    n = dr/nr + 1
    
    print(" + 1/" + str(n), end = " ")
    
    fraction(n*nr-dr, dr*n)
    
    
    
    
    
fraction(2, 12)
print("")
fraction(12, 2)
print("")
fraction(6, 14)
print("")
fraction(12, 13)
print("")
fraction(15, 13)
