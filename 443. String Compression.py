class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        len1 = len(chars)
        if len1 < 2:
            return len1
        buf = chars[0]
        count = 0
        out = ''
        for i in chars:
            if i == buf:
                count += 1
            else:
                out += buf
                if count > 1:
                    out += str(count)
                buf = i
                count = 1
        if count != 1:
            out = out + buf + str(count)
        else:
            out = out + buf
        len1 = len(out)
        for i in range(len1):
            chars[i] = out[i]
        return len1
        
    
print(Solution().compress(["a","a","b","b","c","c","c"]))
print(Solution().compress(["a"]))
print(Solution().compress(["a","b","b","b","b","b","b","b","b","b","b","b","b","b"]))