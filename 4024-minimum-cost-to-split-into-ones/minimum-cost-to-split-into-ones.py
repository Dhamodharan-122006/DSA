class Solution:
    def minCost(self, n: int) -> int:
        s = 0
        for i in range(1,n):
            s += i
        return s
        