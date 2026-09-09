class Solution:
    def isBalanced(self, nums: str) -> bool:
        a = b = 0
        for i in range(0,len(nums),2):
            a += int(nums[i])
            if len(nums)-1 != i:
                b += int(nums[i+1])
            else:
                break
        return a == b
        