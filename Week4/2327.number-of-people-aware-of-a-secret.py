from collections import deque


class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        mod = 1000_000_007
        sharing = 0

        readyQueue = deque([1])
        forgetQueue = deque([1])

        while n > 1:
            if len(readyQueue) >= delay:
                sharing = (sharing + readyQueue.popleft()) % mod
            if len(forgetQueue) >= forget:
                sharing = (sharing + mod - forgetQueue.popleft()) % mod

            readyQueue.append(sharing)
            forgetQueue.append(sharing)
            n -= 1

        return sum(forgetQueue) % mod


print(Solution().peopleAwareOfSecret(4, 1, 3))
