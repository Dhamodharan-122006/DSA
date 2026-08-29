class Solution:
    def checkGoodInteger(self, n: int) -> bool:
        s =0
        sq = 0
        while n != 0:
            last = n % 10
            s += last
            sq += (last*last)
            n = n//10
        return sq - s >= 50