#!/usr/bin/python
# -*- coding:utf-8 -*-
"""
https://www.geeksforgeeks.org/minimum-initial-vertices-traverse-whole-matrix-given-conditions/
"""

def dfs(matrix, visited, sortedlist, row, col, i ,j):
    
    visited[i][j] = True
    
    if i+1 <  row and  visited[i+1][j] is False and matrix[i+1][j] <=  matrix[i][j]:
        dfs(matrix, visited,  sortedlist, row, col, i+1, j)
    
    if i-1 >= 0 and not visited[i-1][j]  and matrix[i-1][j] <=  matrix[i][j]:
        dfs(matrix, visited,  sortedlist, row, col, i-1, j)
        
    if j+1 <  col and not visited[i][j+1]  and matrix[i][j+1] <=  matrix[i][j]:
        dfs(matrix, visited,  sortedlist, row, col, i, j+1)
    
    if j-1 >= 0 and not visited[i][j-1] and  matrix[i][j-1] <=  matrix[i][j]:
        dfs(matrix, visited,  sortedlist, row, col, i, j-1)
    
    



def printSources(matrix, row, col):
    
    
    visited = [[False]*len(matrix[0]) for _ in range(len(matrix))]
    sortedlist = [[matrix[i][j], i ,j]  for i in range(len(matrix[0])) for j in range(len(matrix)) ]
    
    sortedlist = sorted(sortedlist, key = lambda x: x[0]  ,   reverse=True )
    #print(sortedlist)
    #print(visited)
    
    for i in range(len(sortedlist)):
        if visited[sortedlist[i][1]][sortedlist[i][2]] is False:  
            print(sortedlist[i][1],sortedlist[i][2])
            dfs(matrix, visited, sortedlist, row, col, sortedlist[i][1] ,sortedlist[i][2])
    
    
    


if __name__ == "__main__":
    
    matrix =[[ 1, 2, 3],
             [2, 3, 1],
             [1, 1, 1]]
    #print(matrix[0])
    row = len(matrix)
    col = len(matrix[0])
    printSources(matrix, row, col)
    
    
    
