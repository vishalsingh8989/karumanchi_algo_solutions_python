def levelOrder(self, root):
     """
     :type root: TreeNode
     :rtype: List[List[int]]
     """
     if root is None:
         return []
     queue = [root]
     res = []
     
     while queue:
         size = len(queue)
         res.append([])
         for i in xrange(size):
             node = queue.pop(0)
             res[-1].append(node.val)
             if node.left is not None:
                 queue.append(node.left)
             if node.right is not None:
                 queue.append(node.right)
     return res   