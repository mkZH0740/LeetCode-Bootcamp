from typing import Optional, List

from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        queue = deque([(root, 0)])
        levels = {}

        while len(queue) > 0:
            node, level = queue.popleft()
            if level in levels:
                levels[level].append(node)
            else:
                levels[level] = [node]
            if node.left:
                queue.append((node.left, level + 1))
            if node.right:
                queue.append((node.right, level + 1))

        result = []

        for value in levels.values():
            result.append(value[len(value) - 1].val)

        return result
