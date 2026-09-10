class Solution:
    def totalMoney(self, n: int) -> int:
        res = [0,1,2,3,4,5,6,7]
        total = sum(res)
        ct = 1
        if n >= 7:
            n = n - 7
            while n > 7:
                for i in range(1,8):
                    res[i] = res[i] + 1
                total += sum(res)
                ct += 1
                rem = n - 7
                n = rem
            for i in range(1,n+1):
                total = total + (i+ct)
            return total
        else:
            return (n*(n+1))//2
        


        