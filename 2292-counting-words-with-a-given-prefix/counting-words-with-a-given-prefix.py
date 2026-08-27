class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        n = len(pref)
        ct = 0
        for i in words:
            if i[:n] == pref:
                ct += 1
        return ct