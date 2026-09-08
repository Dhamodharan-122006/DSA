class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:

        nums = []

        for row in grid:
            for i in row:
                nums.append(i)

        dic = Counter(nums)

        repeated = 0
        missing = 0

        for k, v in dic.items():
            if v == 2:
                repeated = k

        n = len(nums)

        for i in range(1, n + 1):
            if i not in dic:
                missing = i
                break

        return [repeated, missing]