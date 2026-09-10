class Solution:
    def kthDistinct(self, arr: List[str], n: int) -> str:
        dic = Counter(arr)
        res = []
        for k,v in dic.items():
            if v == 1:
                res.append(k)
        print(res)
        print(n)
        if len(res) >= n:
            return res[n-1]
        else:
            return ""

                