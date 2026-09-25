class Solution:
    def findNumbers(self, nums: list[int]) -> int:
        ct = 0
        for num in nums:
            if len(str(num)) % 2 == 0:
                ct += 1
        return ct
        