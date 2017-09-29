#!/usr/bin/python
__author__ = "Vishal Jasrotia. Stony Brook University"
__copyright__ = ""
__license__ = "GPL"
__version__ = "1.0"
__maintainer__ = "Vishal Jasrotia"
__email__ = "jasrotia.vishal@stonybrook.edu"
__status__ = ""

import os, sys
from linklist import Node


a = Node(1 ,None)
b = Node(2 ,a)
c = Node(3 ,b)
d = Node(4 ,c)
e = Node(5 ,d)
f = Node(6 ,e)
g = Node(7 ,f)
h = Node(8 ,g)
i = Node(9 ,h)
j = Node(10 ,i)
k = Node(11 ,j)
l = Node(12 ,k)
m = Node(13 ,l)
n = Node(14 ,m)


#create circle 
a.setNext(h)

print(a)
slowtemp = n
fasttemp = n
#detect and print 
while slowtemp is not None  and fasttemp is not None :
    sys.stdout.write("%d"%slowtemp.getData())
    slowtemp = slowtemp.getNext()
    fasttemp = fasttemp.getNext().getNext()
    if slowtemp is not None:
        sys.stdout.write(" -> ")

    if slowtemp == fasttemp:
        print("cycle detected in system at %d."%slowtemp.getData())
        break

slowtemp = n
while slowtemp is not None and fasttemp is not None:
    slowtemp = slowtemp.getNext()
    fasttemp = fasttemp.getNext()
    if slowtemp ==fasttemp:
        print("cycle starts from node with data %d"%fasttemp.getData())
        break

