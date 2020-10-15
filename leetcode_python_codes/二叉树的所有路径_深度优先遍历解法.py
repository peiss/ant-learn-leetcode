"""
https://leetcode-cn.com/problems/binary-tree-paths/
"""

from typing import List


class TreeNode:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right

    def __repr__(self):
        val = self.val
        left_val = str(self.left.val if self.left else None)
        right_val = str(self.right.val if self.right else None)
        return f"{val}, {left_val}, {right_val}"


class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        paths = []
        self._dfs(root, "", paths)
        return paths

    def _dfs(self, root: TreeNode, path: str, paths: List[str]):
        if not root:
            return
        path += str(root.val)
        if not root.left and not root.right:
            paths.append(path)
            return

        path = path + "->"
        self._dfs(root.left, path, paths)
        self._dfs(root.right, path, paths)


"""
   1
 /   \
2     3
 \
  5
"""

root = TreeNode(
    1,
    TreeNode(2, None, TreeNode(5)),
    TreeNode(3)
)

s = Solution()
result = s.binaryTreePaths(root)
print(result)
