# 1456. Maximum Number of Vowels in a Substring of Given Length

class Solution(object): 
    def maxVowels(self, s, k): 
        """ 
        :type s: str 
        :type k: int 
        :rtype: int 
        """ 
        len1 = len(s) 
        count = 0 
        vowels = ['a','e','i','o','u'] 
        if len1 <= k: 
            for i in s: 
                if i in vowels: 
                    count += 1 
            return count 
        s = list(s) 
 
        for i in range(k): 
            if s[i] in vowels: 
                count += 1 
        max1 = count 
        for i in range(len1-k): 
            if s[i] in vowels: 
                count -= 1 
            if s[i+k] in vowels: 
                count += 1 
            if count > max1: 
                max1 = count 
        return max1
    
print(Solution().maxVowels("abciiidef", 3))
print(Solution().maxVowels("aeiou", 2))
print(Solution().maxVowels("leetcode", 3))