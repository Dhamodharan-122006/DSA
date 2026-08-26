class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        res = [0]*len(nums)
        odd = 0
        even = 1
        for i in range(0,n):
            res[odd] = nums[i]
            odd += 2
        for i in range(n,len(nums)):
            res[even] = nums[i]
            even += 2
        return res


        