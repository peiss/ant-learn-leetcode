# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

import collections


class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        # 这是一个list[list]，返回最终结果
        result = []
        # 这是一个queue
        queue = collections.deque([root])
        # 只要queue不为空，则循环
        while queue:
            level_size = len(queue)

            curr_level_datas = []
            for _ in range(level_size):
                node = queue.popleft()
                curr_level_datas.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            result.append(curr_level_datas)
        return result