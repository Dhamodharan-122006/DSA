class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        ans = [pref[0]]*(len(pref)+1)
        for i in range(1,len(pref)):
            ans[i] = pref[i-1] ^ pref[i]
        print(ans)
        return ans[:len(pref)]

        