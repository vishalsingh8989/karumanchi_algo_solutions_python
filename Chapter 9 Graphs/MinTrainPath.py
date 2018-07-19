#!/usr/bin/python
# -*- coding:utf-8 -*-
"""
https://www.geeksforgeeks.org/find-the-minimum-cost-to-reach-a-destination-where-every-station-is-connected-in-one-direction/
"""

import sys

INF = float("inf")

def minCostPathDFS(cost):
    
    dist = [INF]*len(cost)
    dist[0] = 0
    
    for i in xrange(len(cost)):
        for j in xrange(i+1, len(cost)):
            if dist[j] >  dist[i] + cost[i][j]: 
                dist[j] = dist[i] + cost[i][j]
    
    return dist[len(cost)-1]

def minCostPath(cost, s, d):
    if s == d :
        return cost[s][d]
    else:
        
        min = cost[s][d]
        for i in xrange(s+1, d):
            c = minCostPath(cost, s, i)  + minCostPath(cost, i, d)
            if c < min:
                min = c
        return min

if __name__ == "__main__":
    cost = [[ 0, 15, 80, 90],
              [INF, 0, 40, 50],
              [INF, INF, 0, 70],
              [INF, INF, INF, 0]
             ]
    print("Min cost is " , minCostPath(cost, 0, len(cost) - 1), minCostPathDFS(cost))
