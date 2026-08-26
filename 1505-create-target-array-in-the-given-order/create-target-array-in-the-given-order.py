class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        res = []
        seen = set()
        for i in range(len(nums)):
                ans =  res[:index[i]] + [nums[i]] + res[index[i]:]
                res = ans
        return res
                        
        