# 1493. Longest Subarray of 1's After Deleting One Element 
 
class Solution(object): 
    def longestSubarray(self, nums): 
        """ 
        :type nums: List[int] 
        :rtype: int 
        """ 
        i = j = count = max1 = 0 
        len1 = len(nums) 
        while i < len1: 
            if nums[i] == 0: 
                count += 1 
            while j < len1 and count > 1: 
                if nums[j] == 0: 
                    count -= 1 
                j += 1 
            max1 = max(i-j,max1) 
            i += 1 
        return max1
    
print(Solution().longestSubarray([1,1,0,1]))
print(Solution().longestSubarray([0,1,1,1,0,1,1,0,1]))
print(Solution().longestSubarray([1,1,1]))