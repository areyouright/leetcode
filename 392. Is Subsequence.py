# 392. Is Subsequence

class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        m = 0
        len1 = len(s)
        len2 = len(t)
        if len1 > len2:
            return False
        elif len1 == len2:
            if s == t:
                return True
            else:
                return False
        for i in s:
            for j in range(m,len2):
                if i == t[j]:
                    m = j+1
                    len1 -= 1
                    break
        if len1 == 0:
            return True
        else:
            return False

print(Solution().isSubsequence("abc","ahbgdc"))
print(Solution().isSubsequence("axc","ahbgdc"))
        