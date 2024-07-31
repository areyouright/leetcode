# 1732. Find the Highest Altitude 
import sys

class Solution(object): 
    def largestAltitude(self, gain): 
        """ 
        :type gain: List[int] 
        :rtype: int 
        """ 
        max1 = -sys.maxsize 
        current = 0 
        for i in gain: 
            current += i 
            max1 = max(max1, current) 
        if max1 < 0: 
            return 0 
        else: 
            return max1
        
print(Solution().largestAltitude([-5,1,5,0,-7]))
print(Solution().largestAltitude([-4,-3,-2,-1,4,3,2]))