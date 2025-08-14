# 14/08/2025
# 2264. Largest 3-Same-Digit Number in String

class Solution:
    def largestGoodInteger(self, num: str) -> str:
        sols=["999","888","777","666","555","444","333","222","111","000"]
        for i in sols:
            if i in num:
                return i
        return ""