class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        min_string = min(strs,key=len)
        prefix = ""
        for index,char in enumerate(min_string):
            for word in strs:
                if word[index] != char:
                    return prefix
            prefix = prefix+char
        return prefix