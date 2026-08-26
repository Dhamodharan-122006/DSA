class Solution:
    def convertDateToBinary(self, date: str) -> str:
        d = date.split("-")
        print(d)
        res = ""
        for ch in d:
            binary = bin(int(ch))[2:]
            res = res + binary + "-"
        return res[0:len(res)-1]
