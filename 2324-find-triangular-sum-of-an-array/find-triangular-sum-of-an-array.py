class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return (nums[0]+nums[1]) % 10
        a = []
        res = [0]*(len(nums)-1)
        while len(res) != 1:
            for i in range(len(nums)-1):
                res[i] = (nums[i]+nums[i+1]) % 10
            nums = res
            if len(nums) == 2:
                a.append(res)
            res = [0]*(len(nums)-1)  
        s = 0
        for row in a:
            for i in row:
                s += i 
        return s % 10   