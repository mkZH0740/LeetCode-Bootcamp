from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return nums[0]

        dp = [nums[0]] * len(nums)

        for step in range(1, len(nums)):
            if nums[step] + dp[step - 1] >= nums[step]:
                dp[step] = nums[step] + dp[step - 1]
            else:
                dp[step] = nums[step]

        return max(dp)
