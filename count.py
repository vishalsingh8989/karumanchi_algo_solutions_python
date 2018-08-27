

import os

c = 0
for root,dirs,files in os.walk(os.getcwd()):
    for file in files:
        if file.endswith(".py"):
            c +=1


print("Number : " ,  c)
    