class Solution:
    def passwordStrength(self, password: str) -> int:
        s = list(set(password))
        print(s)
        lower = 0
        upper = 0
        digit = 0
        symbol = 0
        for ch in s:
            if ch.islower():
                lower += 1
            elif ch.isupper():
                upper += 1
            elif ch.isdigit():
                digit += 1
            else:
                symbol += 1
        res = 0
        while lower > 0:
            res += 1
            lower -= 1
        while upper > 0:
            res += 2
            upper -= 1
        while digit > 0:
            res += 3
            digit -= 1
        while symbol > 0:
            res += 5
            symbol -= 1
        return res
        