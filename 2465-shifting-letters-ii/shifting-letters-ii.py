class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:

        prefix = [0] * (len(s)+1)
        for st,end,d in shifts:
            if d == 1:
                prefix[st] += 1
                prefix[end + 1] -= 1
            else:
                prefix[st] -= 1
                prefix[end + 1] += 1
        curr = 0
        res = []
        for i in range(len(s)):
            curr += prefix[i]
            idx = (ord(s[i]) - 97 + curr) % 26
            res.append(chr(idx+97))
        return "".join(res)
        