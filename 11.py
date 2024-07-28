#11. Container With Most Water

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left_p = 0
        right_p = len(height)-1
        max1 = 0
        if right_p<1:
            return 0
        elif right_p == 1:
            return min(height[0],height[1])
        while left_p < right_p:
            area = min(height[left_p],height[right_p])*(right_p-left_p)
            if area > max1:
                max1 = area
            if height[left_p]>height[right_p]:
                right_p -= 1
            else:
                left_p += 1
        return max1
    
print(Solution().maxArea([1,8,6,2,5,4,8,3,7]))
print(Solution().maxArea([1,1]))

