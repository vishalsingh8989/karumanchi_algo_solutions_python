#!/usr/bin/python
__author__ = "Vishal Jasrotia. Stony Brook University"
__copyright__ = ""
__license__ = "GPL"
__version__ = "1.0"
__maintainer__ = "Vishal Jasrotia"
__email__ = "jasrotia.vishal@stonybrook.edu"
__status__ = ""
__problem__ = 22

import sys
from stacks import *
import random
import time


def timer(f):
    def inner(*args, **kwargs):
        start = time.time()
        f(*args, **kwargs)
        end = time.time()
        print("Execution time : %s"%(end-start))

    return inner

def findspan(entries = []):
    """ time complexity  = O(n2)
    """
    if len(entries) == 0:
        return []
    
    span = []
    for idx, num in enumerate(entries):
        spanidx = idx - 1
        spancount = 1
        while spanidx >=0  and entries[spanidx] <= entries[spanidx + 1]:
            spanidx -=1
            spancount +=1
        span.insert(idx ,  spancount)
    return span
def findspanopt(entries = []):
    """ Time complexity = O(n)
    """ 
    if len(entries) == 0:
        return []

    span = []
    for idx , num in enumerate(entries):
        if idx-1 >=0 and entries[idx-1] < entries[idx]:
            span.insert(idx,span[idx-1] + 1)
        if idx-1 < 0  or entries[idx-1]>= entries[idx]: 
            span.insert(idx, 1)
    return span

        
if __name__ == "__main__":
    entries = random.sample(range(1,1000) ,999)
    print(entries)
    span = findspan(entries)
    print(span)
    span = findspanopt(entries)
    print(span)

