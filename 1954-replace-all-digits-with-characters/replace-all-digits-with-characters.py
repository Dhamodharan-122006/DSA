class Solution:
    def replaceDigits(self, s: str) -> str:
        if len(s) <= 1:
            return s
        s = list(s)
        res = ['']*len(s)
        for i in range(1,len(s),2):
            ans = ord(s[i-1]) + int(s[i])
            res[i-1] = s[i-1]
            res[i] = chr(ans)
        for j in range(i+1,len(s)):
            res[j] = s[j]
        return "".join(res)  