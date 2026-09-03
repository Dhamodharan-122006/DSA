class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        maxi = 0
        window = []
        ct = 0
        for i in range(len(s)):
            if s[i] in "aeiou":
                ct += 1
                window.append(s[i])
            else:
                window.append(s[i])
            if len(window) == k:
                maxi = max(maxi,ct)
                if window[0] in "aeiou":
                    window.pop(0)
                    ct -= 1
                else:
                    window.pop(0) 
        return maxi
        