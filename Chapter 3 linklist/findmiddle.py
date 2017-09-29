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
k = Node(14 ,n)
slowtemp = k
fasttemp = k.getNext()
i = 0
while fasttemp.getNext() is not None :
    if i == 1:
        i = 0
        slowtemp = slowtemp.getNext()
        fasttemp = fasttemp.getNext()
    else:
        fasttemp = fasttemp.getNext()
        i = 1
print("Middle element is %d"%slowtemp.getData())
        
#split list in halfs
newhead = slowtemp.getNext()
slowtemp.setNext(None)
while newhead is not None:
    sys.stdout.write("%d"%newhead.getData())
    newhead = newhead.getNext()
    if newhead is not None:
        sys.stdout.write(" -> ")
print("")

#split list in halfs
newhead = k
while newhead is not None:
    sys.stdout.write("%d"%newhead.getData())
    newhead = newhead.getNext()
    if newhead is not None:
        sys.stdout.write(" -> ")
print("")
