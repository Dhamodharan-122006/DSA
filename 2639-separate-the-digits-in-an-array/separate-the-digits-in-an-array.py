class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        res = []
        for i in range(len(nums)):
            a = str(nums[i])
            for ch in a:
                res.append(int(ch))
        return res
        