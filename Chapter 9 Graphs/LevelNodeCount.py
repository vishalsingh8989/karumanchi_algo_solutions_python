#!/usr/bin/python
# -*-  coding:utf-8 -*-
""" count the nodes on a level using BFS
"""

from _collections import defaultdict

class Tree:
    
    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list)
    
    
    def addEdge(self, u, v):
        self.graph[u].append(v)
    
    def CountOnLevel(self, level):
        
        queue = []
        queue.append(0)
        queue.append("$")
        currlevel = 0
        nodecount = 0
        
        while queue:
            currnode = queue.pop(0)
            #print("pop " + str(currnode))
            if currlevel == level and currnode != "$":
                nodecount += 1
            if currnode == "$":
                if queue:
                    queue.append("$")
                    currlevel += 1
                    #print("Current level + " + str(currlevel))
                    if currlevel > level:
                        return nodecount
            else:
                for v in self.graph[currnode]:
                    queue.append(v)
        return nodecount           
 
if __name__ == "__main__":
    t = Tree(6)
    
    t.addEdge(0, 1)
    t.addEdge(0, 2)
    t.addEdge(1, 3)
    t.addEdge(2, 4)
    t.addEdge(2, 5)
    
    level = 2
    count = t.CountOnLevel(level)
    print("Number of Nodes on level " + str(level) + " = " + str(count))
            