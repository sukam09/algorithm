from itertools import product


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def isValid(s):
            val = 0
            for c in s:
                if c == "(":
                    val += 1
                elif val <= 0:
                    return False
                else:
                    val -= 1
            return val == 0

        pairs = ["(", ")"]
        ans = []

        for p in product(pairs, repeat=n * 2):
            res = "".join(p)
            if isValid(res):
                ans.append(res)

        return ans
