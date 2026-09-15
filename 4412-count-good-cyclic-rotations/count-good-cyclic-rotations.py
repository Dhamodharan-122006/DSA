class Solution:
    def countGoodRotations(self, nums: list[int]) -> int:
        n = len(nums)
        half = n // 2
        total = sum(nums)
        curr = sum(nums[:half])
        ct = 0
        for i in range(n):
            if curr > total - curr:
                ct += 1
            curr = curr - nums[i] + nums[(i + half) % n]
        return ct