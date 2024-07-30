class Solution(object):
    def maxOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        right = len(nums)-1
        left = 0
        count = 0
        nums.sort()
        while left < right:
            sum1 = nums[left] + nums[right]
            if sum1 == k:
                count += 1
                left += 1
                right -= 1
            elif sum1 < k:
                left += 1
            else:
                right -= 1
        return count
    
print(Solution().maxOperations([1,2,3,4], 5))
print(Solution().maxOperations([3,1,3,4,3], 2))