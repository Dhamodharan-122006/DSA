class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        n = len(nums)

        dp = [1] * n
        ct = [1] * n

        for i in range(n):
            for j in range(i):
                if nums[j] < nums[i]:

                    # Found a longer LIS
                    if dp[j] + 1 > dp[i]:
                        dp[i] = dp[j] + 1
                        ct[i] = ct[j]

                    # Found another LIS of same length
                    elif dp[j] + 1 == dp[i]:
                        ct[i] += ct[j]

        longest = max(dp)

        ans = 0
        for i in range(n):
            if dp[i] == longest:
                ans += ct[i]

        return ans