# 1657. Determine if Two Strings Are Close

class Solution(object):
    def closeStrings(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: bool
        """
        len1 = len(word1)
        len2 = len(word2)
        word1 = list(word1)
        word2 = list(word2)
        word1.sort()
        word2.sort()
        buf = word1[0]
        chars = set()
        counts = []
        count = 0
        i = 0
        while i < len1:
            if word1[i] == buf:
                count += 1
            else:
                chars.add(buf)
                counts.append(count)
                buf = word1[i]
                count = 1
            i += 1
        chars.add(buf)
        counts.append(count)
        buf = word2[0]
        i = 0
        count = 0
        while i < len2:
            if word2[i] == buf:
                count += 1
            else:
                try:
                    chars.remove(buf)
                    counts.remove(count)
                except:
                    return False
                buf = word2[i]
                count = 1
            i += 1
        try:
            chars.remove(buf)
            counts.remove(count)
        except:
            return False
        return True

        

print(Solution().closeStrings("abc","bca"))
print(Solution().closeStrings("a","aa"))
print(Solution().closeStrings("cabbba","abbccc"))
print(Solution().closeStrings("xxxxxxxxxxxxxxxxxxx","zzzzzzzzzzzzzzzzzzz"))