class Solution:
    def minMoves(self, nums: List[int]) -> int:
        ct = 0
        maxi = max(nums)
        res = [max(nums)]*len(nums)
        while res != nums:
            for i in range(len(nums)):
                if nums[i] != maxi:
                    nums[i] = nums[i] + 1
                    ct += 1
        return ct

        