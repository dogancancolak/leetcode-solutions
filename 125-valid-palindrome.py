class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        chars = []
        for char in s:
            if char.isalnum():
                chars.append(char.lower())

        left, right = 0, len(chars) - 1
        while left < right:
            if chars[left] != chars[right]:
                return False
            left += 1
            right -= 1

        return True