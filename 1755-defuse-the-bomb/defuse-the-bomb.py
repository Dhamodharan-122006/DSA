class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        window = []
        n = len(code)
        if k > 0:
            s = 0
            ct = 0
            j = 0
            while j < n:
                s = 0
                ct = 0
                for i in range(j,k):
                    s = s + code[(i+1)%n]
                    print(s)
                print("*")
                window.append(s)
                j += 1
                k = k + 1
                print("*",k)
            return window
        elif k < 0:
            s = 0
            ct = 0
            j = 0
            while j < n:
                s = 0
                ct = 0
                for i in range(j,k,-1):
                    s = s + code[(i-1)%n]
                    print(s)
                print("*")
                window.append(s)
                j += 1
                k = k + 1
                print("*",k)
            return window
        else:
            return [0]*n
            


                
