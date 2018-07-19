import matplotlib.pyplot as plt
import time
import sys
def hanoi(numofdisk , startpeg=1, auxpeg = 2 ,endpeg=3):
    if numofdisk:
        hanoi(numofdisk-1, startpeg, endpeg, auxpeg)
        #print("Move %d  disk from %d to %d."%(numofdisk, startpeg, endpeg))
        hanoi(numofdisk-1, auxpeg, startpeg, endpeg)




hanoi(int(sys.argv[1]))

print("****** Done ********")
