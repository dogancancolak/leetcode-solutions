class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        pointer = 0
        if len(needle)> len(haystack):
            return -1
        for i,char in enumerate(haystack):
            if i> len(haystack) - len(needle):
                return -1
            pointer = 0
            if char == needle[0]:
                while pointer < len(needle):
                    if haystack[i] != needle[pointer]:
                        break
                    pointer +=1
                    i+=1
                if pointer == len(needle):
                    return i - pointer
        return -1