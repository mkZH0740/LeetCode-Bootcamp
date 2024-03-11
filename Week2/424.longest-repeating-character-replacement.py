class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        chars = {}

        result = 0

        left = 0
        right = 0

        curr_max = 0

        for right in range(0, len(s)):
            curr_char = s[right]

            chars[curr_char] = chars.get(curr_char, 0) + 1
            curr_max = max(chars[curr_char], curr_max)

            # windows size too big, move left towards right
            if right - left + 1 > k + curr_max:
                chars[s[left]] -= 1
                left += 1
            else:
                result = max(result, right - left + 1)

        return result
