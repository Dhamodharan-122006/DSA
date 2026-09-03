class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        left = 0
        p = sorted(p)
        window = []
        res = []
        for right in range(len(s)):
            window.append(s[right])
            if len(window) > len(p):
                window.pop(0)
                left += 1
            if len(window) == len(p) and sorted(window) == p:
                res.append(left)
        return res

        