#1431. Kids With the Greatest Number of Candies

class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        out = []
        max1 = max(candies)
        for i in candies:
            if i+extraCandies >= max1:
                out.append(True)
            else:
                out.append(False)
        return out
        
print(Solution().kidsWithCandies([2,3,5,1,3], 3))
print(Solution().kidsWithCandies([4,2,1,1,2], 1))
print(Solution().kidsWithCandies([12,1,12], 10))

                                 