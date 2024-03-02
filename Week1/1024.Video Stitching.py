from typing import List


class Solution:
    def videoStitching(self, clips: List[List[int]], time: int) -> int:
        left = -1
        right = 0
        count = 0

        for start, end in sorted(clips):
            if right >= time or start > right:
                # whole segment covered or disjoint found
                break
            elif left < start and start <= right:
                count += 1
                left = right
            right = max(right, end)

        if right >= time:
            return count
        return -1
