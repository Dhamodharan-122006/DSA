class Solution:
    def countSpecialIntegers(self, nums: list[int]) -> int:
        dic = Counter(nums)
        res = defaultdict(list)
        for i,val in enumerate(nums):
            if dic[val] >= 3:
                res[val].append(i)
        ct = 0
        answer = defaultdict(list)
        for key,value in res.items():
            a = res[key]
            for i in range(len(a)-1):
                answer[key].append(a[i+1]-a[i])
        for value in answer.values():
            if len(set(value)) == 1:
                ct += 1
        return ct
                