class Solution:
    def myAtoi(self, s: str) -> int:
        positive = True
        upper_bound = pow(2, 31) - 1
        lower_bound = -pow(2, 31)
        result = 0

        chars = iter(s)

        curr_char = next(chars, None)

        while curr_char == " ":
            curr_char = next(chars, None)

        if curr_char == "-":
            positive = False
            curr_char = next(chars, None)
        elif curr_char == "+":
            positive = True
            curr_char = next(chars, None)

        while curr_char is not None and curr_char >= "0" and curr_char <= "9":
            result = result * 10 + int(curr_char)
            curr_char = next(chars, None)

        if not positive:
            result = -result

        result = min(result, upper_bound)
        result = max(result, lower_bound)

        return result
