class Solution:
    def countAsterisks(self, s: str) -> int:
        s = s.split("|")
        print(s)
        ct = 0
        for i in range(0,len(s),2):
            ct = ct + s[i].count("*")
        return ct