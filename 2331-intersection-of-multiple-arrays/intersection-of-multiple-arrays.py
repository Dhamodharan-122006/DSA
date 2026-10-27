class Solution:
    def intersection(self, nums: list[list[int]]) -> list[int]:
        if len(nums) == 1:
            return sorted(nums[0])
        res = []
        for i in nums:
            res = res + i
        dic = Counter(res)
        maxi = max(dic.values())
        ans = []
        if maxi > 1:
            for key,value in dic.items():
                if value == maxi:
                    ans.append(key)
        else:
            return []
        ans.sort()
        return ans
        

