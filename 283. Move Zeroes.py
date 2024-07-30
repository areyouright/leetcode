#283. Move Zeroes

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        i = 0
        zero = 0
        count = 0
        len1 = len(nums)
        for i in range(len1):
            if nums[i] == 0:
                zero = i
                break
            else:
                count += 1
        if count == len1:
            return nums
        while i < len1:
            if nums[i] != 0:
                nums[i], nums[zero] = nums[zero], nums[i]
                zero += 1
            i += 1
        return nums
    
print(Solution().moveZeroes([0,1,0,3,12]))
print(Solution().moveZeroes([0]))