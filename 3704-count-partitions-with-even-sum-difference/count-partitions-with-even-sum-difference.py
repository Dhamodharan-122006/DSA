class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        ct = 0
        for i in range(len(nums)-1):
            left = sum(nums[:i+1])
            right = sum(nums[i+1:])
            print(left,":",right)
            if abs(left-right) % 2 == 0:
                ct += 1
        return ct
        