class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        len1 = len(flowerbed)-1
        i = 0
        if n == 0:
            return True
        if len1 == 0 and n == 1:
            if flowerbed[0] == 0:
                return True
            else:
                return False
            
        while i <= len1 and n>0:
            if i == 0:
                if flowerbed[0] == 0 and flowerbed[1] == 0:
                    n -= 1
                    i += 2
                else:
                    i += 1
            elif i == len1:
                if flowerbed[i] == 0 and flowerbed[i-1] == 0:
                    n -= 1
                    i += 2
                else:
                    i +=1
            elif flowerbed[i] == 0 and flowerbed[i+1] == 0 and flowerbed[i-1] == 0:
                n -=1
                i += 2
            else: 
                i +=1
        if n>0:
            return False
        else:
            return True
        
print(Solution().canPlaceFlowers([1,0,0,0,1], 1))
print(Solution().canPlaceFlowers([1,0,0,0,1], 2))