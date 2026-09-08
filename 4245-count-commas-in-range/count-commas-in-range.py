class Solution:
    def countCommas(self, n: int) -> int:
        ct = 0
        for i in range(1000,n+1):
            ct += 1
        return ct

        