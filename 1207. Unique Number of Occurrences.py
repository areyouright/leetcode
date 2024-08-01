# 1207. Unique Number of Occurrences

class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        arr.sort()
        count = set()
        len1 = len(arr)
        buf_count = 0
        buf = arr[0]
        i = 0
        while i < len1:
            if arr[i] == buf:
                buf_count += 1
                i += 1
            elif buf_count in count:
                return False
            else:
                count.add(buf_count)
                buf_count = 1
                buf = arr[i]
                i += 1
        if buf_count in count:
            return False
        return True

print(Solution().uniqueOccurrences([1,2,2,1,1,3]))
print(Solution().uniqueOccurrences([1,2]))
print(Solution().uniqueOccurrences([-3,0,1,-3,1,1,1,-3,10,0]))