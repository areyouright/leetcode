class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        mult = 1
        count = 0
        len1 = len(nums)
        for i in nums:
            if i != 0:
                mult *= i
            else:
                count += 1
        if count > 1:
            nums = [0]*len1
        elif count == 1:
            for i in range(len1):
                if nums[i] == 0:
                    nums[i] = mult
                else:
                    nums[i] = 0
        else:
            for i in range(len1):
                nums[i] = mult // nums[i]
        return nums
        
print(Solution().productExceptSelf([1,2,3,4]))
print(Solution().productExceptSelf([-1,1,0,-3,3]))