from modules.queue import Queue
from copy import deepcopy as deepcopy
import sys

class TreeNode:
    def __init__(self, data = None):
        self.data = data
        self.left = None
        self.right = None
    
    def __repr__(self):
        if self.right is None:
            right =  "right(None)"
        else:
            right = "right(" +str(self.right.val)+ ")"
             
        if self.left is None:
            left = "left(None)"
        else:
            left = "left(" +str(self.left.val)+ ")"
            
        rpr = "[ " + left + ", " +str(self.val) + ", " + right + " ]" 
        return rpr
        
    def visit(self):
        sys.stdout.write(self.data)
    
    def getNumNodes(self):
        total = 0
        if self.left:
          total += self.left.getNumNodes()
        if self.right:
          total += self.right.getNumNodes()
        return total + 1
    
    
    @classmethod
    def createTree(cls, depth):
        tree = Node('X')
        cls.createTreeHelper(tree, depth, 1)
        return tree
    
    @classmethod
    def createTreeHelper(cls, node, depth, cur):
        if cur == depth:
          return
        node.left = Node('X')
        node.right = Node('XX')
        cls.createTreeHelper(node.left, depth, cur + 1)
        cls.createTreeHelper(node.right, depth, cur + 1)
    
    
    def getHeight(self):
        return TreeNode.getHeightHelper(self)
    
    @staticmethod
    def getHeightHelper(node):
        if not node:
          return 0
        else:
          return max(TreeNode.getHeightHelper(node.left), TreeNode.getHeightHelper(node.right)) + 1
    
    def fillTree(self, height):
        TreeNode.fillTreeHelper(self, height)
    
    def fillTreeHelper(node, height):
        if height <= 1:
          return
        if node:
          if not node.left: node.left = TreeNode(' ')
          if not node.right: node.right = TreeNode(' ')
          TreeNode.fillTreeHelper(node.left, height - 1)
          TreeNode.fillTreeHelper(node.right, height - 1)
    
    
    def prettyPrint(self):
        """
        """
        # get height of tree
        total_layers = self.getHeight()
        print("Total layers", total_layers)
        tree = deepcopy(self)
    
        tree.fillTree(total_layers)
        # start a queue for BFS
        queue = Queue()
        # add root to queue
        queue.enqueue(tree) # self = root
        # index for 'generation' or 'layer' of tree
        gen = 1 
        # BFS main
        while not queue.isEmpty():
          # copy queue
          # 
          copy = Queue()
          while not queue.isEmpty():
            copy.enqueue(queue.dequeue())
          # 
          # end copy queue 
    
          first_item_in_layer = True
          edges_string = ""
          extra_spaces_next_node = False
    
          # modified BFS, layer by layer (gen by gen)
          while not copy.isEmpty():
    
            node = copy.dequeue()
    
            # -----------------------------
            # init spacing
            spaces_front = pow(2, total_layers - gen + 1) - 2
            spaces_mid   = pow(2, total_layers - gen + 2) - 2
            dash_count   = pow(2, total_layers - gen) - 2
            if dash_count < 0:
              dash_count = 0
            spaces_mid = spaces_mid - (dash_count*2)
            spaces_front = spaces_front - dash_count
            init_padding = 2
            spaces_front += init_padding
            if first_item_in_layer:
              edges_string += " " * init_padding
            # ----------------------------->
    
            # -----------------------------
            # construct edges layer
            edge_sym = "/" if node.left and node.left.data is not " " else " "
            if first_item_in_layer:
              edges_string += " " * (pow(2, total_layers - gen) - 1) + edge_sym
            else:
              edges_string += " " * (pow(2, total_layers - gen + 1) + 1) + edge_sym
            edge_sym = "\\" if node.right and node.right.data is not " " else " "
            edges_string += " " * (pow(2, total_layers - gen + 1) - 3) + edge_sym
            # ----------------------------->
    
            # -----------------------------
            # conditions for dashes
            if node.left and node.left.data == " ":
              dash_left = " "
            else:
              dash_left = "_"
    
            if node.right and node.right.data == " ":
              dash_right = " "
            else:
              dash_right = "_"
            # ----------------------------->
    
            # -----------------------------
            # handle condition for extra spaces when node lengths don't match or are even:
            if extra_spaces_next_node:
              extra_spaces = 1
              extra_spaces_next_node = False
            else:
              extra_spaces = 0
            # ----------------------------->
            
            # -----------------------------
            # account for longer data
            data_length = len(str(node.data))
            if data_length > 1:
              if data_length % 2 == 1: # odd
                if dash_count > 0:
                  dash_count -= ((data_length - 1)/2)
                else:
                  spaces_mid -= (data_length - 1)/2
                  spaces_front -= (data_length - 1)/2
                  if data_length is not 1: 
                    extra_spaces_next_node = True 
              else: # even
                if dash_count > 0:
                  dash_count -= ((data_length)/2) - 1
                  extra_spaces_next_node = True
                  # dash_count += 1
                else:
                  spaces_mid -= (data_length - 1)
                  spaces_front -= (data_length - 1)
            # ----------------------------->
            
            # -----------------------------
            # print node with/without dashes
            if first_item_in_layer:
              print (" " * spaces_front) + (dash_left * dash_count) + str(node.data) + (dash_right * dash_count),
              first_item_in_layer = False
            else:
              print (" " * (spaces_mid-extra_spaces)) + (dash_left * dash_count) + str(node.data) + (dash_right * dash_count),
            # ----------------------------->
    
            if node.left: queue.enqueue(node.left)
            if node.right: queue.enqueue(node.right)
    
          # print the fun squiggly lines
          if not queue.isEmpty():
            print "\n" + edges_string
    
          # increase layer index
          gen += 1
          

class BTNode:
    def __init__(self, val, left = None, right = None):
        self.val  = val
        self.left = left
        self.right = right
    
    def __repr__(self):
        if self.right is None:
            right =  "right(None)"
        else:
            right = "right(" +str(self.right.val)+ ")"
             
        if self.left is None:
            left = "left(None)"
        else:
            left = "left(" +str(self.left.val)+ ")"
            
        rpr = "[ " + left + ", " +str(self.val) + ", " + right + " ]" 
        return rpr
    

def stringToTreeNode(input):
    #input = input.strip()
    #input = input[1:-1]
    if not input:
        return None

    inputValues = input  # [s.strip() for s in input.split(',')]
    root = TreeNode(inputValues[0])
    nodeQueue = [root]
    front = 0
    index = 1
    while index < len(inputValues):
        node = nodeQueue[front]
        front = front + 1

        item = inputValues[index]
        index = index + 1
        if (type(item) is str and item != "null" ) or type(item) is int:
            leftNumber = int(item)
            node.left = TreeNode(leftNumber)
            nodeQueue.append(node.left)

        if index >= len(inputValues):
            break

        item = inputValues[index]
        index = index + 1
        if (type(item) is str and item != "null" ) or type(item) is int:
            rightNumber = item
            node.right = TreeNode(rightNumber)
            nodeQueue.append(node.right)
    return root