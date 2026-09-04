class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:

        n=len(nums)
        pref=[0]*n
        suff=[0]*n
        idx=-1
        mini=float("inf")
        pref[0]=nums[0]
        suff[-1]=nums[-1]

        for i in range(1,n):
            pref[i]=max(pref[i-1],nums[i])
        for i in range(n-2,-1,-1):
            suff[i]=min(suff[i+1],nums[i])

        for i in range(n-1,-1,-1):
            left=pref[i]
            right=suff[i]
        

            if left-right<=k :
                mini=left-right
                idx=i
        return idx
        