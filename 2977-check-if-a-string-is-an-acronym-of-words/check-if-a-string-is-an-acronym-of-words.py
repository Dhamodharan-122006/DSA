class Solution:
    def isAcronym(self, words: List[str], s: str) -> bool:
        first_ch = []
        for word in words:
            first_ch.append(word[0])
        ct = 0
        if len(words) == len(s):
            for ch in range(len(first_ch)):
                if first_ch[ch] == s[ch]:
                    ct += 1
            return ct == len(s)
        else:
            return False

        