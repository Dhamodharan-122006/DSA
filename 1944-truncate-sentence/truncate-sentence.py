class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        words = s.split()
        res = ""
        ct = 0
        for i in words:
            if ct != k:
                res = res + i + " "
                ct += 1
        return res.rstrip(" ")

        