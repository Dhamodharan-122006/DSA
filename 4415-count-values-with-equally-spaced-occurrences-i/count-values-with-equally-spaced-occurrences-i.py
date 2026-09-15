class Solution:
    def countSpecialIntegers(self, nums: list[int]) -> int:
        dic = Counter(nums)
        res = defaultdict(list)
        for i,val in enumerate(nums):
            if dic[val] == 3:
                res[val].append(i)
        print(res)
        ct = 0
        for value in res.values():
            a = value
            if a[1]-a[0] == a[2]-a[1]:
                ct += 1
        return ct
                