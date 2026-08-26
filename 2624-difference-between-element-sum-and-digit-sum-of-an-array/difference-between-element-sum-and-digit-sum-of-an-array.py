class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        element = 0
        digit = 0
        for i in nums:
            element += i
        print(element)
        res = []
        for i in nums:
            res.append(str(i))
        for i in range(len(res)):
            a = res[i]
            for ch in a:
                digit += int(ch)
        return abs(element - digit)
        