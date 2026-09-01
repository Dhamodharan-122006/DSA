class Solution:
    def closestTarget(self, words: List[str], target: str, startIndex: int) -> int:
        diff = float("inf")
        n = len(words)
        if target not in words:
            return -1 
            exit()
        for i in range(n):
            if words[i] == target:
                d = abs(i-startIndex)
                diff = min(diff,min(d,n-d))
        return diff
                  
            



        