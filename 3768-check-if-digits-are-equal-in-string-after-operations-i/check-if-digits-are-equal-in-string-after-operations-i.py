class Solution:
    def hasSameDigits(self, s: str) -> bool:
        s = list(s)
        n = len(s)
        res = ""
        while len(s) != 2:
            res = ""
            for i in range(len(s)-1):
                a = int((int(s[i])+int(s[i+1]))) % 10
                res += str(a)
            s = res
        return res[0] == res[1]