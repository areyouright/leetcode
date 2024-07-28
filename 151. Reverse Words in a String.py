class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        s_new = []
        buf = ''
        for i in s:
            if i != ' ':
                buf += i
            else:
                s_new.append(buf)
                buf = ''
        if s[-1] != ' ':
            s_new.append(buf)
        s = ''
        for i in reversed(s_new):
            if i != '':
                s = s + ' ' + i
        return s.replace(' ','',1)

print(Solution().reverseWords("the sky is blue"))
print(Solution().reverseWords("  hello world  "))
print(Solution().reverseWords("a good   example"))