class Solution:
    def countDigitOccurrences(self, nums: list[int], digit: int) -> int:
        n = [str(i) for i in nums]
        d = str(digit)
        ct = 0
        for i in range(len(n)):
            ct = ct + n[i].count(d)
        return ct
        