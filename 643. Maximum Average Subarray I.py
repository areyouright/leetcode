# 643. Maximum Average Subarray I

class Solution(object): 
    def findMaxAverage(self, nums, k): 
        """ 
        :type nums: List[int] 
        :type k: int 
        :rtype: float 
        """ 
        sum1 = max1 = sum(nums[0:k]) 
        len1 = len(nums) 
        for i in range(0,len1-k): 
            sum1 = sum1 - nums[i] + nums[i+k] 
            if sum1 > max1: 
                max1 = sum1 
        return float(max1)/float(k)

print(Solution().findMaxAverage([1,12,-5,-6,50,3], 4))
print(Solution().findMaxAverage([5], 1))