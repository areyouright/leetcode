#1071. Greatest Common Divisor of Strings

class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        len1 = len(str1)
        len2 = len(str2)
        min_l = min(len1,len2)
        out = ''
        i = ''
        while len(i) < min_l:
            i += str2[len(i)]
            count1  = len1//len(i)
            count2 = len2//len(i)
            if (i*count1 == str1) and (i*count2 == str2):
                out = i
        return out

print(Solution().gcdOfStrings('ABCABC', 'ABC'))  # Output: 'ABC'
print(Solution().gcdOfStrings('ABABAB', 'ABAB'))  # Output: 'ABAB'
print(Solution().gcdOfStrings('LEETCODE', 'CODE'))  # Output: ''