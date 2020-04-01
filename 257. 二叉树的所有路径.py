# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if not root:
            return []
        result_list = []
        self._dfs(root, "", result_list)

        return result_list

    def _dfs(self, root, path: str, result_list: List):
        """
        node_list: single node list
        reslt_list: final list
        """
        if not root:
            return ""

        path += str(root.val)
        if not root.left and not root.right:
            result_list.append(path)

        path += "->"
        if root.left:
            self._dfs(root.left, path, result_list)
        if root.right:
            self._dfs(root.right, path, result_list)


"""
   1
 /   \
2     3
 \
  5
"""

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.right = TreeNode(5)

s = Solution()
print(s.binaryTreePaths(root))
