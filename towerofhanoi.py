def hanoi(numofdisk , startpeg=1, auxpeg = 2 ,endpeg=3):
    if numofdisk:
        hanoi(numofdisk-1, startpeg, endpeg, auxpeg)
        print("Move %d  disk from %d to %d."%(numofdisk, startpeg, endpeg))
        hanoi(numofdisk-1, auxpeg, startpeg, endpeg)


def karumanchi_hanoi(numofdisk , startpeg=1, endpeg=3):
    if numofdisk:
        karumanchi_hanoi(numofdisk-1, startpeg, 6-startpeg-endpeg)
        print("Move %d  disk from %d to %d."%(numofdisk, startpeg, endpeg))
        karumanchi_hanoi(numofdisk-1, 6-startpeg-endpeg, endpeg)

hanoi(3)
print("******************")
karumanchi_hanoi(3)
