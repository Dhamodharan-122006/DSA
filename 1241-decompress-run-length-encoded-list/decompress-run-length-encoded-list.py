class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        res = []
        i = 0
        while i < len(nums):
            j = i + 1
            for _ in range(0,nums[i]):
                res.append(nums[j])
            i += 2
        return res
            
        