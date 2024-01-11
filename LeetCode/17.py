from itertools import product


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return []

        map = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }
        ans = []
        cand = []
        for digit in digits:
            cand.append(map[digit])
        for p in product(*cand):
            ans.append("".join(p))
        return ans
