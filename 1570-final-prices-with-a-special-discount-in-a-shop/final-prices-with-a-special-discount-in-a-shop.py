class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        ans = []
        flag = False
        for i in range(len(prices)):
            ct = 0
            for j in range(i+1,len(prices)):
                if prices[j] <= prices[i]:
                    ans.append(abs(prices[j]-prices[i]))
                    ct += 1
                    break
            if ct == 0:
                ans.append(prices[i])
        return ans
        