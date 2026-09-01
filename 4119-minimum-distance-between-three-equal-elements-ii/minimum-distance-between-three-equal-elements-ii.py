class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        dic = defaultdict(list)
        for idx,value in enumerate(nums):
            dic[value].append(idx)
        mini = float("inf")
        for key in dic.values():
            n = len(key)
            if n >= 3:
                for i in range(n-2):
                    x = key[i]
                    y = key[i+1]
                    z = key[i+2]
                    mini = min(mini,(2*(z-x)))
        return mini if mini != float("inf") else -1

        