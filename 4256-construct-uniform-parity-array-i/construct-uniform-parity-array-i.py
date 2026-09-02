class Solution:
    def uniformArray(self, nums: list[int]) -> bool:
        res = [0]*len(nums)
        odd = 0
        for i in range(len(res)):
            if nums[i] % 2 == 1:
                odd = nums[i]
                break
        for i in range(len(res)):
            if nums[i] % 2 == 0:
                res[i] = nums[i] - odd
            else:
                res[i] = nums[i]
        if all(i % 2 == 0 for i in res):
            return True
        else:
            flag = False
        if flag == False:
            return True
        



        