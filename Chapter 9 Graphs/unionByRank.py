__author__ = "Vishal Jasrotia"
__copyright__ = "Copyright 2018"
__credits__ = ["Vishal Jasrotia"]
__license__ = "GPL"
__version__ = "1.0.1"
__maintainer__ = "Vishal Jasrotia"
__email__ = "jasrotia.vishal@stonybrook.edu"
__status__ = "Production"


class Node:
    """
    """
    def __init__(self):
        """
        """
        self.data = None
        self.parent = None
        self.rank = 0
        
class DSU:
    """
    
    class for disjoint set union
    
    """
    
    def __init__(self):
        """
        """
        self.map = {}
    
    
    def makeSet(self, data):
        """
        """
        node = Node()
        node.data = data
        node.parent = node
        node.rank = 0
        self.map[data] = node
    
    
    def union(self, u,v):
        """
        """
        node_u = self.map[u]
        node_v = self.map[v]
        
        
        node_u_parent = self.findParent(node_u)
        node_v_parent = self.findParent(node_v)
        
        if node_u_parent.data == node_v_parent.data:
            return
        
        #The node with higher rank become the parent of other
        if node_u_parent.rank >=  node_v_parent.rank:
            # increment the rank of parent if rank is same
            node_u_parent.rank = node_u_parent.rank + 1 if node_u_parent.rank == node_v_parent.rank else  node_u_parent.rank
            node_v_parent.parent = node_u_parent
        else:
            node_u_parent.parent = node_v_parent
            
        
        
    def findSet(self, u):
        """ find sets representative node and return data
        """
        node = self.map[u]
        node_parent = self.findParent(node)
        return node_parent.data
    
    def findParent(self, node):
        """ find representative and compress on return by setting representative(top node) as parent of every child on that path.
        """
        node_parent = node.parent
        if(node_parent == node):
            return node_parent
                
        node.parent = self.findParent(node.parent)
        return node.parent


        
if __name__ == "__main__":
    dsu = DSU()
    
    for i in xrange(12):
        dsu.makeSet(i)
    
    dsu.union(0,1)
    dsu.union(1,2)
    dsu.union(2,3)
    dsu.union(0,7)
    
    dsu.union(4,8)
    dsu.union(8,11)
    
    dsu.union(5,6)
    dsu.union(9,10)
    dsu.union(6,9)
    
    print(dsu.map)
    
    for i in xrange(12):
        print(i , dsu.findSet(i))
    

