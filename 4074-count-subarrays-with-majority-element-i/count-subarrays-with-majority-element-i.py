class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        count = 0
        for i in range(len(nums)):
            ct = 0
            for j in range(i,len(nums)):
                if nums[j] == target:
                    ct += 1
                length = j - i + 1
                if ct > length // 2:
                    count += 1
        return count
        
        