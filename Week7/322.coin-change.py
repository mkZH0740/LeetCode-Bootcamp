import math
from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [math.inf] * (amount + 1)
        dp[0] = 0

        for step in range(1, amount + 1):
            for coin in coins:
                if coin <= step:
                    dp[step] = min(dp[step], 1 + dp[step - coin])

        if dp[-1] != math.inf:
            return dp[-1]

        return -1
