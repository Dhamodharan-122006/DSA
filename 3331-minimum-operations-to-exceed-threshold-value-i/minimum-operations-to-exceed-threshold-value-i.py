class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        ct = 0
        for i in range(len(nums)):
            if nums[i] < k:
                ct += 1
        return ct
        