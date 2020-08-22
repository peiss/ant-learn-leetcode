# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

import collections

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        queue = collections.deque([root])
        level = 0
        while queue:
            level += 1
            level_size = len(queue)
            for _ in range(level_size):
                node = queue.popleft()
                if not node.left and not node.right: return level
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)

        return level

