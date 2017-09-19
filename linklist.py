import sys

class Node(object):

    def validate(f):
        def wrapper(*args, **kwargs):
            if not isinstance(args[1], Node) and args[1] is not None:
                raise Exception("Second argument should be either None or obj of class  Node")
            else:
                f(*args,**kwargs)
        return wrapper
                


    def __new__(cls, data, nextNode):
        print("In __new__")
        if not isinstance(nextNode, Node) and nextNode is not None :
            raise Exception("Second argument should be either None or obj of class  Node")
        else:
            return super(Node, cls).__new__(cls, data, nextNode)
    
    def __init__(self, data, nextNode):
        """check  validity of nextNode in __new__. If not valid then dont init.
        """
        self._data     = data
        self._nextNode = nextNode
    
    @validate
    def setNext(self, nextNode):
        self._nextNode = nextNode

    def getNext(self):
        return self._nextNode

    def setData(self, _data):
        self._data = data

    def getData(self):
        return self._data



def insertAtBegin(head, data):
    node  = Node(data, head) # create new node which will be newh head poitiong to previuos head and return new node(new head)
    return node

def printLinklist(head):
    while(head.getData() is not None and head.getNext() is not None):
        sys.stdout.write("%d  "%(head.getData()))
        head = head.getNext()
        if head.getData() is not None:
            sys.stdout.write(" -> ")
    print("")


def CreateLinklist():
    print(" Creating link list with empty head.")
    return Node(None,None)

