class Solution:
    def findDisappearedNumbers(self, nums: list[int], lower: int, upper: int) -> list[list[int]]:

        missing = []

        seen = set(nums)

        for i in range(lower, upper + 1):
            if i not in seen:
                missing.append(i)

        nums.sort()

        final = []
        j = 0

        if not missing:
            return []

        for i in range(len(nums)):
            num = nums[i]
            res = []

            while j < len(missing) and missing[j] < num:
                res.append(missing[j])
                j += 1

            if res:
                final.append(res)

        res = []

        for k in range(j, len(missing)):
            res.append(missing[k])

        if res:
            final.append(res)

        for row in final:
            if len(row) == 1:
                row.append(row[0])

        new = []

        for row in final:
            if len(row) > 2:
                new.append([row[0], row[-1]])
            elif len(row) == 2:
                new.append(row)

        return new