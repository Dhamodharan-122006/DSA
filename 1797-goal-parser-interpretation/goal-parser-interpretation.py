class Solution:
    def interpret(self, command: str) -> str:
        res = ""
        ans = ""
        for i in range(len(command)):
            res += command[i]
            if res == 'G':
                ans += 'G'
                res = ""
            elif res == '(al)':
                ans += 'al'
                res = ""
            elif res == '()':
                ans += 'o'
                res = ""
        return ans
        