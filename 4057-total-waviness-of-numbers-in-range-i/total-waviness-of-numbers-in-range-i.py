class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        s = 0
        for i in range(num1,num2+1):
            n = str(i)
            num = list(n)
            print(num)
            for j in range(1,len(num)-1):
                if int(num[j-1]) < int(num[j]) and int(num[j]) > int(num[j+1]):
                    s += 1
                if int(num[j-1]) > int(num[j]) and int(num[j]) < int(num[j+1]):
                    s += 1
        return s


        