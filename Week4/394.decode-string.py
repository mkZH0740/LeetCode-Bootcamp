class Solution:
    def decodeString(self, s: str) -> str:
        return self.recursiveDecodeString(s, 0)[1]

    def recursiveDecodeString(self, s: str, index: int):
        result = ""

        while index < len(s) and s[index] != "]":
            currChar = s[index]
            if currChar.isnumeric():
                k = ""
                while index < len(s) and currChar.isnumeric():
                    k += currChar
                    index += 1
                    currChar = s[index]
                kNum = int(k)

                index += 1
                index, wrappedStr = self.recursiveDecodeString(s, index)
                index += 1

                result += wrappedStr * kNum
            else:
                result += currChar
                index += 1

        return index, result


Solution().decodeString("3[a2[c]]")
