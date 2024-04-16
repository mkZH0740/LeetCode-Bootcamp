from typing import Set, Dict, List


class Solution:
    def dfs(self, s: str, wordSet: Set[str], memo: Dict[str, bool]):
        if s in memo:
            return memo[s]
        if s in wordSet:
            return True

        for i in range(1, len(s)):
            prefix = s[:i]
            suffix = s[i:]

            if prefix in wordSet and self.dfs(suffix, wordSet, memo):
                memo[s] = True
                return True
        memo[s] = False
        return False

    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        return self.dfs(s, set(wordDict), {})
