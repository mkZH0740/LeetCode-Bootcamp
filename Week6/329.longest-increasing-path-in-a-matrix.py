from typing import List


class Solution:
    def dfs(self, matrix: List[List[int]], row: int, col: int, prev: int, memo: dict):
        if row < 0 or col < 0:
            return 0
        if row >= len(matrix) or col >= len(matrix[0]):
            return 0

        curr = matrix[row][col]

        if curr <= prev:
            return 0

        curr_key = f"{row} {col}"

        if curr_key in memo:
            return memo[curr_key]

        length = 1
        length = max(self.dfs(matrix, row + 1, col, curr, memo) + 1, length)
        length = max(self.dfs(matrix, row - 1, col, curr, memo) + 1, length)
        length = max(self.dfs(matrix, row, col + 1, curr, memo) + 1, length)
        length = max(self.dfs(matrix, row, col - 1, curr, memo) + 1, length)

        memo[curr_key] = length
        return length

    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        memo = {}
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                self.dfs(matrix, row, col, -1, memo)
        return max(memo.values())
