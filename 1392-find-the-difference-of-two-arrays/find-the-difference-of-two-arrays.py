class Solution:
    def findDifference(self, nums1: list[int], nums2: list[int]) -> list[list[int]]:
        a = set()
        b = set()
        for i in range(len(nums1)):
            if nums1[i] not in nums2:
                a.add(nums1[i])
            
        for j in range(len(nums2)):
            if nums2[j] not in nums1:
                b.add(nums2[j])
        return [list(a),list(b)]