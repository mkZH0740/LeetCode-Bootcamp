from typing import List


class Solution:
    def reverse(self, word: str):
        return word[::-1]

    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        words_dict = {}
        result = []

        for index, word in enumerate(words):
            words_dict[word] = index

        for index, word in enumerate(words):
            word_reverse = self.reverse(word)

            if "" in words_dict and words_dict[""] != index and word_reverse == word:
                result.append([index, words_dict[""]])

            for substr_length in range(len(word)):
                leading_substr = word[: substr_length + 1]
                remaining_substr = word[substr_length + 1 :]

                leading_reverse = self.reverse(leading_substr)
                remaining_reverse = self.reverse(remaining_substr)

                if (
                    leading_reverse in words_dict
                    and words_dict[leading_reverse] != index
                    and remaining_substr == remaining_reverse
                ):
                    result.append([index, words_dict[leading_reverse]])
                if (
                    remaining_reverse in words_dict
                    and words_dict[remaining_reverse] != index
                    and leading_substr == leading_reverse
                ):
                    result.append([words_dict[remaining_reverse], index])

        return result
