class Solution:
    def minLengthAfterRemovals(self, s: str) -> int:
        if s.count("a") == s.count("b"):
            return 0
        elif (s.count("a") > 0 and s.count("b") == 0) or (s.count("a") == 0 and s.count("b") > 0):
            return len(s)
        else:
            if s.count("a") > s.count("b"):
                return s.count("a") - s.count("b")
            else:
                return s.count("b") - s.count("a")
        
        