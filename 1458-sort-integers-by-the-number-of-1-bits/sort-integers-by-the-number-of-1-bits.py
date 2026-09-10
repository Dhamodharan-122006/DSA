class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        res = []
        dic = defaultdict(list)
        for i in range(len(arr)):
            dic[bin((arr[i])).count("1")].append(arr[i])
        print(dic)
        for k in sorted(dic.keys()):
            for val in sorted(dic[k]):
                res.append(val)
        return res