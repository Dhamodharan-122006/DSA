class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m = len(s)+1
        n = len(t)+1
        dp = [[0]*n for _ in range(m)]
        for i in range(m):
            dp[i][0] = 1
        for i in range(1,m):
            for j in range(1,n):
                dp[i][j] = dp[i-1][j]
                if s[i-1] == t[j-1]:
                    dp[i][j] += dp[i-1][j-1]
        return dp[m-1][n-1]