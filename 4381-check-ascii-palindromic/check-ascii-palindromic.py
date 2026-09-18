class Solution:
    def isPalindromic(self, s: str) -> bool:
        res = ""
        for ch in s:
            a = ord(ch)
            res = res + bin(a)
        x = res.replace("b"," ")
        answer = x.split()
        final = "".join(answer)
        return final == final[::-1]