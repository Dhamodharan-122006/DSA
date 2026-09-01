class Solution:
    def getDistances(self, arr: List[int]) -> List[int]:
        dic = defaultdict(list)
        for i,v in enumerate(arr):
            dic[v].append(i)
        res = [0]*len(arr)
        for key in dic.values():
            n = len(key)
            if n >= 2:
                total = sum(key)
                left = 0
                for i in range(n):
                    curr = key[i]
                    right = total - left - curr
                    res[curr] = curr * i - left + right - curr*(n-i-1)
                    left += curr
        return res
        