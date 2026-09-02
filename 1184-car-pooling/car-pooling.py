class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        prefix = [0]*(1001)
        for n,f,t in trips:
            prefix[f] += n
            prefix[t] -= n
        print(prefix)

        res = []
        ans = 0
        for num in prefix:
            ans += num
            res.append(ans)
        maxi = max(res)
        if maxi <= capacity:
            return True
        else:
            return False