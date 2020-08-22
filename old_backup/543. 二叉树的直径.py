# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def depth(self, root: TreeNode):
        """
        求二叉树的深度
        """
        if not root:
            return 0
        left_depth = self.depth(root.left)
        right_depth = self.depth(root.right)
        # 左右深度节点数的和
        self.result = max(self.result, left_depth + right_depth)
        return max(left_depth, right_depth) + 1

    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        # 默认是root的1个节点
        self.result = 0
        self.depth(root)
        return self.result


"""
          1
         / \
        2   3
       / \     
      4   5    
"""
root = TreeNode(1)
root.left = TreeNode(2)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right = TreeNode(3)
s = Solution()
print(s.diameterOfBinaryTree(root))
