class Solution:
    def sortSentence(self, s: str) -> str:
        s = s.split()
        nums = []
        for i in range(len(s)):
            for ch in range(len(s[i])):
                if s[i][ch].isdigit():
                    nums.append(s[i][ch])
        nums.sort()
        res = []
        for i in range(len(nums)):
            for j in range(len(s)):
                if nums[i] in s[j]:
                    res.append(s[j])
        ans = ""
        for ch in range(len(res)):
            n = len(res[ch])
            a = res[ch]
            ans = ans + a[:n-1] + " "
        return ans.strip(" ")

        