class Solution:
    def minOperations(self, nums: List[int]) -> int:
        ct = 0
        j = 0
        res = nums
        for i in range(len(nums)-2):
            if nums[i] == 0:
                if nums[i] == 0:
                    nums[i] = 1
                else:
                    nums[i] = 0
                if nums[i+1] == 0:
                    nums[i+1] = 1
                else:
                    nums[i+1] = 0
                if nums[i+2] == 0:
                    nums[i+2] = 1

                else:
                    nums[i+2] = 0
                ct += 1
        if len(set(nums)) == 1:
            return ct
        return -1