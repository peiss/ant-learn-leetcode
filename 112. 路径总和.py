# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def _dfs(self, root, curr_sum: int, sum: int) -> bool:
        if not root:
            return False

        curr_sum += root.val

        if not root.left and not root.right and curr_sum == sum:
            return True

        return self._dfs(root.right, curr_sum, sum) or self._dfs(root.left, curr_sum, sum)

    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root:
            return False
        return self._dfs(root, 0, sum)


"""
              5
             / \
            4   8
           /   / \
          11  13  4
         /  \      \
        7    2      1
"""

root = TreeNode(5)
root.left = TreeNode(4)
root.left.left = TreeNode(11)
root.left.left.left = TreeNode(7)
root.left.left.right = TreeNode(2)
root.right = TreeNode(8)
root.right.left = TreeNode(13)
root.right.right = TreeNode(4)
root.right.right.right = TreeNode(1)

s = Solution()
print(s.hasPathSum(root, 22))
