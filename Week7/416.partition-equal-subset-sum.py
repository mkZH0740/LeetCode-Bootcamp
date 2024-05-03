from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        length = len(nums)
        total = sum(nums)

        if total % 2 != 0:
            return False

        k = total // 2
        prev = []

        for _ in range(k + 1):
            prev.append(False)

        prev[0] = True

        if nums[0] <= k:
            prev[nums[0]] = True

        for index in range(1, length):
            curr = []
            for _ in range(k + 1):
                curr.append(False)
            for target_index in range(1, k + 1):
                curr[0] = True
                pick = False
                not_pick = prev[target_index]

                if target_index >= nums[index]:
                    pick = prev[target_index - nums[index]]
                curr[target_index] = pick or not_pick
            prev = curr[:]
        return prev[k]
