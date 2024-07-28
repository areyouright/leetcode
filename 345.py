class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        right_p = len(s)-1
        left_p = 0
        s = list(s)
        vowels = ['a','e','i','o','u']
        while left_p < right_p:
            if s[left_p].lower() in vowels:
                if s[right_p].lower() in vowels:
                    s[left_p], s[right_p] =  s[right_p], s[left_p]
                    left_p +=1
                    right_p -= 1
                else:
                    right_p -= 1
            else:
                left_p += 1
        return ''.join(s)
        
print(Solution().reverseVowels("hello"))
print(Solution().reverseVowels("leetcode"))