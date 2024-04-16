# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def lowestCommonAncestor(
        self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
    ) -> "TreeNode":
        if root is None:
            return None

        if root == p or root == q:
            return root

        leftSubTree = self.lowestCommonAncestor(root.left, p, q)
        rightSubTree = self.lowestCommonAncestor(root.right, p, q)

        if leftSubTree and rightSubTree:
            return root

        return leftSubTree or rightSubTree
