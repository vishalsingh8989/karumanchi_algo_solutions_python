class Node(object):
    def __init__(self, key, prev, next_):
        self.next = next_
        self.prev = prev
        self.key = key

class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity=capacity
        self.cache = {}
        self.ll_head = None
        self.ll_tail = None
        

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.cache:
            self._move_to_head(self.cache[key][1])
            return self.cache[key][0]
        else:
            return -1
        

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if key in self.cache:
            self.cache[key] = (value, self.cache[key][1])
            self._move_to_head(self.cache[key][1])
            return
        if len(self.cache) == self.capacity:
            self._evict()
        if len(self.cache) == 0:
            node = self._init_dll(key)
        else:
            node = self._insert_new_to_head(key)
        self.cache[key] = (value, node)
     
     
     
        
    def _init_dll(self, key):
        node = Node(key, None, None)
        self.ll_head = node
        self.ll_tail = node
        return node
    
    def _insert_new_to_head(self, key):
        node = Node(key, None, self.ll_head)
        self.ll_head.prev = node
        self.ll_head = node
        return node
        
    def _insert_new_to_tail(self, key):
        node = Node(key, self.ll_tail, None)
        self.ll_tail.next = node
        self.ll_tail = node
        return node
    
    def _move_to_head(self, node):
        if node == self.ll_head:
            return
        if node == self.ll_tail:
            self.ll_tail = node.prev
        node.prev.next = node.next
        if node.next:
            node.next.prev = node.prev
        node.prev = None
        node.next = self.ll_head
        node.next.prev = node
        self.ll_head = node
        
    def _evict(self):
        del self.cache[self.ll_tail.key]
        if len(self.cache) == 0:
            self.ll_tail = None
            self.ll_head = None
        else:
            new_tail = self.ll_tail.prev
            self.ll_tail.prev.next = None
            self.ll_tail = new_tail
        

if __name__ == "__main__":
    # Your LRUCache object will be instantiated and called as such:
    obj = LRUCache(3)
    param_1 = obj.get(3)
    obj.put(3,2)
    print(obj.get(3))