class Solution:
    def reverseDegree(self, s: str) -> int:
        alpha = "abcdefghijklmnopqrstuvwxyz"
        ct=26
        dic = {}
        for i in alpha:
            dic[i] = ct
            ct -= 1
        ans = 0
        idx = 1
        for i in range(len(s)):
            ans = ans + (idx*dic[s[i]])
            idx += 1
        return ans