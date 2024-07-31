# 724. Find Pivot Index

class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 1
        left = 0
        right = sum(nums[1:])
        len1 = len(nums)
        while left != right and i < len1  :
            left += nums[i-1]
            right -= nums[i]
            i += 1
        if left == right:
            return(i-1)
        else:
            return -1
        
print(Solution().pivotIndex([1, 7, 3, 6, 5, 6]))
print(Solution().pivotIndex([2, -1, 1]))
print(Solution().pivotIndex([-1,-1,-1,-1,-1,0]))