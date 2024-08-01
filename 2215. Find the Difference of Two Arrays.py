# 2215. Find the Difference of Two Arrays

class Solution(object):
    def findDifference(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[List[int]]
        """
        nums1_b = set(nums1)
        nums2_b = set(nums2)
        nums2_b.difference_update(set(nums1))
        nums1_b.difference_update(set(nums2))
        return [nums1_b,nums2_b]
            
print(Solution().findDifference([1,2,3],[2,4,6]))
print(Solution().findDifference([1,2,3,3],[1,1,2,2]))