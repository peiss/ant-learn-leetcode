# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        # 如果都是None，认定是一样
        if not p and not q:
            return True

        # 如果哪一边不为None，则为False
        # 注意这时候已经都不为None了
        if not p or not q:
            return False

        # 如果都不是None，那么先判断数据值是否相同
        if p.val != q.val:
            return False

        # 走到这里，说明root节点已经相同了，那么递归比较孩子即可
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
