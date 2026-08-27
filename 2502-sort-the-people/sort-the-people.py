class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        dic = {}
        for i in range(len(heights)):
            dic[heights[i]] = names[i]
        print(dic)
        res = []
        for k,v in sorted(dic.items(),reverse = True):
            res.append(v)
        return res

        