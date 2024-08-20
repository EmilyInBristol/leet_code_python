class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        
        hs_len = len(haystack)
        start = -1
        i = 0
        mark = -1
        while i < hs_len:
            if haystack[i] == needle[0]:
                start = i
                mark = i
                j = 0
                while j < len(needle) and start < hs_len:
                    if needle[j] != haystack[start]:
                        break
                    j += 1
                    start += 1
                    
                if j == len(needle):
                    return start - j
                else:
                    i = mark + 1
                    continue
            i += 1
        return -1