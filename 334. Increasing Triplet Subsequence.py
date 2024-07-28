import sys

class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) < 3:
            return False
        first = sys.maxsize
        second = sys.maxsize
        for i in nums:
            if i <= first:
                first = i
            elif i <= second:
                second = i
            else:
                return True
        return False

print(Solution().increasingTriplet([1,2,3,4,5]))
print(Solution().increasingTriplet([5,4,3,2,1]))