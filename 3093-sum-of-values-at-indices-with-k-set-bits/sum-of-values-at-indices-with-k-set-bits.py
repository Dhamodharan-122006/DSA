class Solution:
    def sumIndicesWithKSetBits(self, nums: List[int], k: int) -> int:
        n = len(nums)
        res = []
        for i in range(n):
            res.append(bin(i)[2:])
        ans = 0
        for i in range(len(res)):
            a = str(res[i])
            if a.count('1') == k:
                ans += nums[i]
        return ans
        