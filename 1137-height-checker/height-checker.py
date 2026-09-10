class Solution:
    def heightChecker(self, h: List[int]) -> int:
        ct = 0
        e = sorted(h)
        for i in range(len(h)):
            if h[i] != e[i]:
                ct += 1
        return ct
        