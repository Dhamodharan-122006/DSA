class Solution:
    def numberOfMatches(self, n: int) -> int:
        matches = 0
        while n != 1:
            curr = n
            if curr % 2 == 1:
                matches = matches + (curr-1)//2
                curr = ((curr-1)//2)+1
            else:
                matches = matches + (curr//2)
                curr = (curr//2)
            n = curr
        return matches