"""
https://www.geeksforgeeks.org/a-linked-list-with-next-and-arbit-pointer/
"""

class Node:
    def __init__(self, data, next, random):
        self.data = data
        self.next = next
        self.random = random
    def __repr__(self):
        if self.next is not None:
            return " [ " + str(self.data) + ", " + str(self.next.data) + ", " + str(self.random.data) + " ] "
        return " [ " + str(self.data) + ", None , " + str(self.random.data) + " ] "
    
    
def copyList(head):
    pass

if __name__ == "__main__":
    one = Node(10, None, None)
    two = Node(20, one, None)
    three = Node(30, two, None)
    four = Node(40, three, None)
    five = Node(50, four, None)
    six = Node(60, five, None)
    seven = Node(70, six, None)
    
    one.random = six
    two.random = seven
    three.random = one
    four.random = two
    five.random = three
    six.random = four
    seven.random = five
    
    print(one)
    print(two)
    print(three)

