from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        node = root
        curr_count = 0

        while node is not None or len(stack) > 0:
            while node is not None:
                stack.append(node)
                node = node.left

            node = stack.pop()
            curr_count += 1
            if curr_count == k:
                return node.val
            # move to next subtree
            node = node.right

        return 0
