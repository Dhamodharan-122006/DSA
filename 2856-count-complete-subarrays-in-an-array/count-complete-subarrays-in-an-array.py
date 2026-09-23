class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        k = len(set(nums))
        ct = 0
        for i in range(len(nums)):
            res = set()
            for j in range(i,len(nums)):
                res.add(nums[j])
                if len((res)) == k:
                    ct += 1     
        return ct