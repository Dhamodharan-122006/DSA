class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        from collections import defaultdict

        dic = defaultdict(list)

        a = ["type", "color", "name"]

        for row in items:
            for i in range(len(row)):
                dic[a[i]].append(row[i])

        return dic[ruleKey].count(ruleValue)





        