# 1323. Maximum 69 Number(16/08/2025)
class Solution:
    def maximum69Number(self, num: int) -> int:
        s=list(str(num))
        for i in range (len(s)):
            if s[i]=='9':
                s[i]='6'
                break
        return (' '.join(s))
