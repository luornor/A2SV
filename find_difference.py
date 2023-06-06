class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        res = ''
        for ch in t:
            if ch not in s:
                res = ''.join(ch)
            elif t.count(ch)>s.count(ch):
                res = ''.join(ch)

        return res 