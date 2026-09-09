class Solution:
    def addedInteger(self, nums1: List[int], nums2: List[int]) -> int:
        nums1.sort()
        nums2.sort()
        diff = nums2[0] - nums1[0]
        for i in range(len(nums1)):
            nums1[i] = nums1[i] + diff
        return diff
        