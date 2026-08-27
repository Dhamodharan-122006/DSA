class Solution:
    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        ct = 0
        for i in range(len(nums1)):
            if nums1[i] in nums2:
                ct += 1
        res.append(ct)
        c = 0
        for j in range(len(nums2)):
            if nums2[j] in nums1:
                c += 1
        res.append(c)
        return res

        