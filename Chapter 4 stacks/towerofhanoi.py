


def towerofhanoi(n, from_rod, to_rod, aux_rod):
    if n == 1:
        print("Move disk %s from %s to %s"%(n, from_rod, to_rod))
        return 
    
    towerofhanoi(n-1, from_rod, aux_rod, to_rod)
    print("Move disk %s from %s to %s"%(n, from_rod, to_rod))
    towerofhanoi(n-1, aux_rod, to_rod, from_rod)



def findLegalMovesBetween(rodSrc, rodDst, src, dst):
    
    if rodSrc and rodDst:
        if rodSrc[-1] <  rodDst[-1]:
            disk = rodSrc.pop()
            print("Move disk %s from %s to %s"%(disk, src, dst))
            rodDst.append(disk)
        else:
            disk = rodDst.pop()
            print("Move disk %s from %s to %s"%(disk, dst, src))
            rodSrc.append(disk)
    elif rodSrc:
        disk = rodSrc.pop()
        print("Move disk %s from %s to %s"%(disk, src, dst))
        rodDst.append(disk)
    elif rodDst:
        disk = rodDst.pop()
        print("Move disk %s from %s to %s"%(disk, dst, src))
        rodSrc.append(disk)
    else:
        print("Illegal move")
    
def towerofhanoiItr(n):
    numofmoves = pow(2,n)
    
    rodSrc = list(range(n, 0, -1))
    rodDst = []
    rodAux = []
    
    src = "A"
    dst = "C"
    aux = "B"
    print(rodSrc, rodAux, rodDst)
    if n%2 == 0:
        aux, dst = dst, aux
    
    for i in xrange(1, numofmoves ):
        if i%3 == 1:
            findLegalMovesBetween(rodSrc, rodDst, src, dst)
        elif i%3 == 2:
            findLegalMovesBetween(rodSrc, rodAux, src, aux)
        elif i%3 == 0:
            findLegalMovesBetween(rodAux, rodDst, aux, dst)
        
    print(rodSrc, rodAux, rodDst)
    
if __name__ == "__main__":
    towerofhanoi(5, "A", "C", "B")
    print("******************")
    towerofhanoiItr(5)