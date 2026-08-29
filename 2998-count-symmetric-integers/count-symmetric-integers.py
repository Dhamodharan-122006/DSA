class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        nums = [str(i) for i in range(low,high+1)]
        ct = 0
        for i in range(len(nums)):
            n = len(nums[i])//2
            a = nums[i]

            if len(a) % 2 == 0:
                first = a[:n]
                f = 0
                for i in first:
                    f += int(i)
                second = a[n:]
                s = 0
                for i in second:
                    s += int(i)
                if f == s:
                    ct += 1
        return ct



        