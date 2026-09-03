class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        col = m
        row = n
        dp = [[0]*n for _ in range(col)]
        dp[0][0] = 1
        for i in range(col):
            dp[i][0] = 1
        for j in range(row):
            dp[0][j] = 1
        for i in range(1,col):
            for j in range(1,row):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[col-1][row-1]

        