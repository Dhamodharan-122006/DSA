class Solution:
    def kidsWithCandies(self, nums: List[int], k: int) -> List[bool]:
        maxi = max(nums)
        res = [False]*len(nums)
        for i in range(len(nums)):
            ans = nums[i] + k
            if ans >= maxi:
                res[i] = True
        return res

        