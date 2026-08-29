class Solution:
    def elevatorRequests(self, n: int, req: list[int]) -> int:
        s = 0
        curr = 0
        for i in range(len(req)):
            s = s + abs(curr - req[i])
            curr = req[i]
        return s 

        
        


        