# 1004. Max Consecutive Ones III 
 
from collections import deque as dq 
 
class Solution(object): 
    def longestOnes(self, nums, k): 
        """ 
        :type nums: List[int] 
        :type k: int 
        :rtype: int 
        """ 
 
        max1 = count = i = 0 
        sub_nums = dq() 
        len1 = len(nums) 
        while i < len1: 
            if nums[i] == 0: 
                count += 1 
            sub_nums.append(nums[i]) 
            if count > k: 
                max1 = max(len(sub_nums)-1, max1) 
            while count > k: 
                if sub_nums[0] == 0: 
                    count -= 1 
                sub_nums.popleft() 
            i += 1 
        return max(max1,len(sub_nums))
    
print(Solution().longestOnes([1,1,1,0,0,0,1,1,1,1,0],2))
print(Solution().longestOnes([0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1],3))