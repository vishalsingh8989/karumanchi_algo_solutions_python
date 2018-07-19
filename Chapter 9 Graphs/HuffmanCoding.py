#!/usr/bin/python
"""
https://www.geeksforgeeks.org/greedy-algorithms-set-3-huffman-coding/
"""
__author__ = "Vishal Jasrotia. Stony Brook University"
__copyright__ = ""
__license__ = "GPL"
__version__ = "1.0"
__maintainer__ = "Vishal Jasrotia"
__email__ = "jasrotia.vishal@stonybrook.edu"
__status__ = ""

class Node:
    def __init__(self, l, f, left = None, right = None):
        self.letter = l
        self.freq = f
        self.left = left
        self.right = right
    def __repr__(self):
        return str(self.letter) + "-" + str(self.freq)

class HuffmanCode:
    
    def __init__(self, l, f):
        self.nodes = []
        for i in xrange(len(l)):
            self.nodes.append(Node(l[i], f[i]))
        
        size = len(l)
        for i in xrange(size/2 + 1 , -1 , -1):
            self.heapify(i, size)
        
        #print(self.nodes)
        
    
    def heapify(self, i ,size):
        smallest = i
        left_child = 2*i + 1 
        right_child = 2*i + 2
        
        if left_child <  size  and self.nodes[left_child].freq < self.nodes[smallest].freq:
            smallest = left_child
        
        if right_child <  size  and self.nodes[right_child].freq <  self.nodes[smallest].freq:
            smallest = right_child
        
        if smallest != i:
            self.nodes[smallest] , self.nodes[i] = self.nodes[i], self.nodes[smallest]
            self.heapify(smallest, size)
    
    def getMin(self):
        node = self.nodes.pop(0)
        self.heapify(0, len(self.nodes))
        return node
        
    def buildHuffmanTree(self):
        
        while len(self.nodes) > 1:
            left = self.getMin()
            right = self.getMin()
            new_node = Node("*", left.freq + right.freq, left, right)
            self.nodes.insert(0, new_node)
            self.heapify(0, len(self.nodes))
        
        return self.nodes[0]
            
    def printCode(self, node, s):
        if node.letter != "*":
            print(node.letter + " = " + s)
        else:
            self.printCode(node.left, s + "0") 
            self.printCode(node.right, s + "1") 
            
if __name__ == "__main__":
    charArray = [ 'f', 'e'  , 'd' , 'c', 'b' ,'a']
    charfreq = [ 45, 16, 13, 12, 9, 5 ]
    huffman = HuffmanCode(charArray,charfreq)
    root = huffman.buildHuffmanTree()
    huffman.printCode(root, "")
    
    
    
    
    
    