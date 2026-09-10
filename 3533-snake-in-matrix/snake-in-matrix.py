class Solution:
    def finalPositionOfSnake(self, n: int, commands: List[str]) -> int:
        res = [[0]*n for _ in range(n)]
        idx = 0
        for row in res:
            a = row
            for i in range(len(a)):
                a[i] = idx
                idx += 1
        i , j = 0, 0
        for ch in commands:
            if ch == "DOWN":
                i += 1
            elif ch == "RIGHT":
                j += 1
            elif ch == "LEFT":
                j -= 1 
            elif ch == "UP":
                i -= 1
        return res[i][j]
