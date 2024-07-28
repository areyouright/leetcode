class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        out = ''
        len1 = len(word1)
        len2 = len(word2)
        i = 0
        while i < max(len1,len2):
            if i < len1:
                out += word1[i]
            if i <len2:
                out += word2[i]
            i +=1
        return out
        
print(Solution().mergeAlternately('abc', 'def'))
print(Solution().mergeAlternately('ab', 'pqrs'))
print(Solution().mergeAlternately('abcd', 'pq'))