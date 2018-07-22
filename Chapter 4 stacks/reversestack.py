#!/usr/bin/python
__author__ = "Vishal Jasrotia. Stony Brook University"
__copyright__ = ""
__license__ = "GPL"
__version__ = "1.0"
__maintainer__ = "Vishal Jasrotia"
__email__ = "jasrotia.vishal@stonybrook.edu"
__status__ = ""

import sys

from stacks import *

def insertAtBottom(st, num):
    if st.size() == 0 :
        st.push(num)
    else:
        n = st.pop()
        insertAtBottom(st, num)
        st.push(n)

def reversestack1(st):
    if st.size() > 0:
        num = st.pop()
        reversestack1(st)
        insertAtBottom(st, num)
    
#O(n) space
def reversestack(st):
    t = Stack()
    while st.size() !=0:
        t.push(st.pop())
    return t




if __name__ == "__main__":
    st =Stack()
    for x in range(7):
        st.push(x)
    st.printstack()
    st = reversestack(st)
    print("******************8")
    st.printstack()
    reversestack1(st)
    print("******************8")
    st.printstack()



