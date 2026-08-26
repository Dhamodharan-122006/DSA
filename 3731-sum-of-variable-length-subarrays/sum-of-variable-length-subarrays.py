class Solution:
    def subarraySum(self, nums: List[int]) -> int:
        s = 0
        start = 0
        for i in range(len(nums)):
            start = max(0,i-nums[i])
            print(nums[start:i])
            s += sum(nums[start:i+1])
        return s
        